"""FrankEnergie API implementation."""
# python_frank_energie/frank_energie.py

import asyncio
from datetime import date, datetime, timedelta, timezone
from http import HTTPStatus
import re
from typing import Any, Optional
import logging
from urllib import response

_LOGGER = logging.getLogger(__name__)

import aiohttp
import requests
import sys
import platform
from aiohttp import ClientResponse, ClientSession, ClientError

from .authentication import Authentication
from .exceptions import (AuthException, AuthRequiredException,
                         FrankEnergieException, NetworkError,
                         RequestException)
from .models import (Authentication, EnergyConsumption, EnodeChargers, EnodeVehicles, Invoices,
                     MarketPrices, Me, MonthInsights, MonthSummary,
                     PeriodUsageAndCosts, SmartBatteries, SmartBattery, SmartBatteryDetails, SmartBatterySummary, SmartBatterySessions, User, UserSites)

VERSION = "2025.9.30"

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

class FrankEnergieQuery:
    """Represents a GraphQL query for the FrankEnergie API."""

    def __init__(self, query: str, operation_name: str, variables: dict[str, Any] | None = None) -> None:
        if variables is not None and not isinstance(variables, dict):
            raise TypeError("The 'variables' argument must be a dictionary if provided.")

        self.query = query
        self.operation_name = operation_name
        self.variables = variables if variables is not None else {}

    def to_dict(self) -> dict[str, Any]:
        """Convert the query to a dictionary suitable for GraphQL API calls."""
        return {
            "query": self.query,
            "operationName": self.operation_name,
            "variables": self.variables,
        }


def sanitize_query(query: FrankEnergieQuery) -> dict[str, Any]:
    sanitized_query = query.to_dict()
    if "password" in sanitized_query["variables"]:
        sanitized_query["variables"]["password"] = "****"
    return sanitized_query


class FrankEnergie:
    """FrankEnergie API client."""

    DATA_URL = "https://frank-graphql-prod.graphcdn.app/"
    # DATA_URL = "https://graphql.frankenergie.nl/"

    def __init__(
        self,
        clientsession: Optional[ClientSession] = None,
        auth_token: Optional[str] = None,
        refresh_token: Optional[str] = None,
        version: str | None = None,
    ) -> None:
        """Initialize the FrankEnergie client."""
        self._session: Optional[ClientSession] = clientsession
        self._close_session: bool = clientsession is None
        self._auth: Optional[Authentication] = None

        if auth_token or refresh_token:
            self._auth = Authentication(auth_token, refresh_token, version)

    is_smart_charging = False
    is_smart_trading = False

    async def close(self) -> None:
        """Close the client session if it was created internally."""
        if self._close_session and self._session is not None:
            await self._session.close()

    @property
    def auth(self) -> Optional[Authentication]:
        """Backwards compatibility for integrations accessing .auth directly."""
        _LOGGER.error("Using .auth directly is deprecated. Use .is_authenticated instead.")
        return self._auth

    @property
    def is_authenticated(self) -> bool:
        """Check if the client is authenticated."""
        return self._auth is not None and self._auth.authToken is not None

    @staticmethod
    def generate_system_user_agent() -> str:
        """Generate the system user-agent string for API requests."""
        system = platform.system()  # e.g., 'Darwin' for macOS, 'Windows' for Windows
        system_platform = sys.platform  # e.g., 'win32', 'linux', 'darwin'
        release = platform.release()  # OS version (e.g., '10.15.7')
        version = VERSION  # App version

        user_agent = f"FrankEnergie/{version} {system}/{release} {system_platform}"
        return user_agent

    async def _ensure_session(self) -> None:
        """Ensure that a ClientSession is available."""
        if self._session is None:
            self._session = ClientSession()
            self._close_session = True

    async def _query(self,
                     query: FrankEnergieQuery,
                     extra_headers: dict[str, str] | None = None
    ) -> dict[str, Any]:
        """Send a query to the FrankEnergie API.

        Args:
            query: The GraphQL query as a dictionary.

        Returns:
            The response from the API as a dictionary.

        Raises:
            NetworkError: If the network request fails.
            FrankEnergieException: If the request fails.
        """

            # "User-Agent": self.generate_system_user_agent(), # not working properly
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        if self._auth is not None and self._auth.authToken is not None:
            headers["Authorization"] = f"Bearer {self._auth.authToken}"

        if extra_headers:
            headers.update(extra_headers)

        self._last_query = query
        self._last_variables = query.variables
        self._operation_name = query.operation_name

        # print(f"Request: POST {self.DATA_URL}")
        # print(f"Request headers: {headers}")
        _LOGGER.debug("Request headers: %s", headers)
        # print(f"Request payload: {query}")
        # print(f"Request payload: {query.to_dict()}")
        if isinstance(query, dict):
            _LOGGER.debug("Request payload: %s", query)
        else:
            _LOGGER.debug("Request payload: %s", query.to_dict())

        await self._ensure_session()

        try:
            if hasattr(query, "to_dict") and callable(query.to_dict):
                payload = query.to_dict()
            else:
                _LOGGER.error("Query object does not implement to_dict() method: %s", query)
                # print(f"Query object does not implement to_dict() method: {query}")
                raise TypeError("Query object must implement a to_dict() method to be JSON serializable.", query)
            async with self._session.post(
                self.DATA_URL,
                json=payload,
                headers=headers,
                timeout=30
            ) as resp:
                resp.raise_for_status()
                response: dict[str, Any] = await resp.json()

            # self._process_diagnostic_data(response)
            if not response:
                _LOGGER.debug("No response data.")
                return {}

            logging.debug("Response body: %s", response)
            self._handle_errors(response)

            # print(f"Response status code: {response.status}")
            # print(f"Response headers: {response.headers}")
            # print(f"Response body: {response}")
            return response

        except (asyncio.TimeoutError, ClientError, KeyError) as error:
            _LOGGER.error("Request failed: %s", error)
            raise NetworkError(f"Request failed: {error}") from error
        except aiohttp.ClientResponseError as error:
            if error.status == HTTPStatus.UNAUTHORIZED:
                raise AuthRequiredException("Authentication required.") from error
            elif error.status == HTTPStatus.FORBIDDEN:
                raise AuthException("Forbidden: Invalid credentials.") from error
            elif error.status == HTTPStatus.BAD_REQUEST:
                raise RequestException("Bad request: Invalid query.") from error
            elif error.status == HTTPStatus.INTERNAL_SERVER_ERROR:
                raise FrankEnergieException("Internal server error.") from error
            else:
                raise FrankEnergieException(f"Unexpected response: {error}") from error
        # except Exception as error:
        #     _LOGGER.exception("Unexpected error during query: %s", error)
#            raise FrankEnergieException("Unexpected error occurred.") from error
        except Exception as error:
            import traceback
            traceback.print_exc()
            raise error

    def _process_diagnostic_data(self, response: dict[str, Any]) -> None:
        """Process the diagnostic data and update the sensor state.

        Args:
            response: The API response as a dictionary.
        """
        diagnostic_data = response.get("diagnostic_data")
        if diagnostic_data:
            self._frank_energie_diagnostic_sensor.update_diagnostic_data(
                diagnostic_data)

    def _handle_errors(self, response: dict[str, object]) -> None:
        """Catch common error messages and raise a more specific exception.

        Args:
            response: The API response as a dictionary.
        """
        # _LOGGER.debug("Handling errors in response: %s", response)

        if not response:
            _LOGGER.debug("No response data.")
            return

        errors = response.get("errors")
        if not errors:
            return

        for error in errors:
            message = error["message"]
            path = error["path"] if "path" in error else None
            if message == "user-error:password-invalid":
                raise AuthException("Invalid password")
            elif message == "user-error:auth-not-authorised":
                raise AuthException("Not authorized")
            elif message == "user-error:auth-required":
                raise AuthRequiredException("Authentication required")
            elif message == "Graphql validation error":
                _LOGGER.error("Request failed %s", self)
                _LOGGER.error("Request query %s", getattr(self, "query", "<unknown>")),
                _LOGGER.error("Graphql validation error: %s %s (%s)", message, path, response)
                raise FrankEnergieException(
                    "Request failed: Graphql validation error — check query and variables.")
            elif message.startswith("No marketprices found for segment"):
                # raise FrankEnergieException("Request failed: %s", error["message"])
                return
            elif message.startswith("No connections found for user"):
                raise FrankEnergieException(
                    "Request failed: %s", message)
            elif message == "user-error:smart-trading-not-enabled":
                _LOGGER.debug("Smart trading is not enabled for this user.")
                # raise SmartTradingNotEnabledException(
                #     "Smart trading is not enabled for this user.")
                return None
            elif message == "user-error:smart-charging-not-enabled":
                _LOGGER.debug("Smart charging is not enabled for this user.")
                # raise SmartChargingNotEnabledException(
                #     "Smart charging is not enabled for this user.")
                return None
            elif message == "'Base' niet aanwezig in prijzen verzameling":
                _LOGGER.debug("'Base' niet aanwezig in prijzen verzameling %s.", path)
            elif message == "request-error:request-not-supported-in-country":
                _LOGGER.error("Request not supported in the user's country: %s", error)
                return None
            else:
                _LOGGER.error("Unhandled error: %s", message)
                _LOGGER.error("Unhandled error in GraphQL response: %s", error)

    LOGIN_QUERY = """
        mutation Login($email: String!, $password: String!) {
            login(email: $email, password: $password) {
                authToken
                refreshToken
                __typename
            }
            version
            __typename
        }
    """

    async def login(self, username: str, password: str) -> Authentication:
        """Login and retrieve the authentication token.

        Args:
            username: The user's email.
            password: The user's password.

        Returns:
            The authentication information.

        Raises:
            AuthException: If the login fails.
        """
        if not username or not password:
            raise ValueError("Username and password must be provided.")

        query = FrankEnergieQuery(
            self.LOGIN_QUERY,
            "Login",
            {"email": username, "password": password}
        )

        try:
            response = await self._query(query)
            # auth_data = None
            if response is not None:
                data = response["data"]
                if data is not None:
                    # auth_data = data["login"]
                    self._auth = Authentication.from_dict(response)
            return self._auth

        except Exception as error:
            import traceback
            traceback.print_exc()
            raise error

    async def renew_token(self) -> Authentication:
        """Renew the authentication token.

        Returns:
            The renewed authentication information.

        Raises:
            AuthRequiredException: If the client is not authenticated.
            AuthException: If the token renewal fails.
        """
        if self._auth is None or not self.is_authenticated:
            raise AuthRequiredException("Authentication is required.")

        query = FrankEnergieQuery(
            """
            mutation RenewToken($authToken: String!, $refreshToken: String!) {
                renewToken(authToken: $authToken, refreshToken: $refreshToken) {
                    authToken
                    refreshToken
                }
            }
            """,
            "RenewToken",
            {
                "authToken": self._auth.authToken,
                "refreshToken": self._auth.refreshToken,
            },
        )

        response = await self._query(query)
        self._auth = Authentication.from_dict(response)
        return self._auth

    async def meter_readings(self, site_reference: str) -> EnergyConsumption:
        """Retrieve the meter_readings.

        Args:
            month: The month for which to retrieve the summary. Defaults to the current month.

        Returns:
            The Meter Readings.

        Raises:
            AuthRequiredException: If the client is not authenticated.
            FrankEnergieException: If the request fails.
        """
        if self._auth is None or not self.is_authenticated:
            raise AuthRequiredException("Authentication is required.")

        query = FrankEnergieQuery(
            """
            query ActualAndExpectedMeterReadings($siteReference: String!) {
            completenessPercentage
            actualMeterReadings {
                date
                consumptionKwh
            }
            expectedMeterReadings {
                date
                consumptionKwh
            }
            }
            """,
            "ActualAndExpectedMeterReadings",
            {"siteReference": site_reference},
        )

        response = await self._query(query)
        return EnergyConsumption.from_dict(response)

    async def month_summary(self, site_reference: str) -> MonthSummary:
        """Retrieve the month summary for the specified month.

        Args:
            month: The month for which to retrieve the summary. Defaults to the current month.

        Returns:
            The month summary information.

        Raises:
            AuthRequiredException: If the client is not authenticated.
            FrankEnergieException: If the request fails.
        """
        if self._auth is None or not self.is_authenticated:
            raise AuthRequiredException("Authentication is required.")

        query = FrankEnergieQuery(
            """
            query MonthSummary($siteReference: String!) {
                monthSummary(siteReference: $siteReference) {
                    _id
                    actualCostsUntilLastMeterReadingDate
                    expectedCostsUntilLastMeterReadingDate
                    expectedCosts
                    lastMeterReadingDate
                    meterReadingDayCompleteness
                    gasExcluded
                    __typename
                }
                version
                __typename
            }
            """,
            "MonthSummary",
            {"siteReference": site_reference},
        )

        try:
            response = await self._query(query)
            return MonthSummary.from_dict(response)
        except Exception as e:
            raise FrankEnergieException(
              f"Failed to fetch month summary: {e}"
              ) from e

    async def enode_chargers(self, site_reference: str, start_date: date) -> dict[str, EnodeChargers]:
        """Retrieve the enode charger information for the specified site reference.

        Args:
            site_reference: The site reference for which to retrieve the enode charger information.
            start_date: The start date for filtering the enode charger information.

        Returns:
            The enode charger information.

        Raises:
            AuthRequiredException: If the client is not authenticated.
            FrankEnergieException: If the request fails.
        """
        if self._auth is None or not self.is_authenticated:
            _LOGGER.debug("Skipping Enode Chargers: not authenticated.")
            return {}
            # raise AuthRequiredException("Authentication is required.")

        query = FrankEnergieQuery(
            """
            query EnodeChargers {
                enodeChargers {
                    canSmartCharge
                    chargeSettings {
                        calculatedDeadline
                        capacity
                        deadline
                        hourFriday
                        hourMonday
                        hourSaturday
                        hourSunday
                        hourThursday
                        hourTuesday
                        hourWednesday
                        id
                        initialCharge
                        initialChargeTimestamp
                        isSmartChargingEnabled
                        isSolarChargingEnabled
                        maxChargeLimit
                        minChargeLimit
                    }
                    chargeState {
                        batteryCapacity
                        batteryLevel
                        chargeLimit
                        chargeRate
                        chargeTimeRemaining
                        isCharging
                        isFullyCharged
                        isPluggedIn
                        lastUpdated
                        powerDeliveryState
                        range
                    }
                    id
                    information {
                        brand
                        model
                        year
                    }
                    interventions {
                        description
                        title
                    }
                    isReachable
                    lastSeen
                }
            }
            """,
            "EnodeChargers",
            {"siteReference": site_reference},
        )

        try:

            # response = await self._query(query)
            response: dict[str, Any] = await self._query(query)
            # Response data for testing purposes
            # mock_response = {'data': {'enodeChargers': [{'canSmartCharge': True, 'chargeSettings': {'calculatedDeadline': '2025-03-24T06:00:00.000Z', 'capacity': 75, 'deadline': None, 'hourFriday': 420, 'hourMonday': 420, 'hourSaturday': 420, 'hourSunday': 420, 'hourThursday': 420, 'hourTuesday': 420, 'hourWednesday': 420, 'id': 'cm3rogazq06pz13p8eucfutnx', 'initialCharge': 0, 'initialChargeTimestamp': '2024-11-21T19:00:15.396Z', 'isSmartChargingEnabled': True, 'isSolarChargingEnabled': False, 'maxChargeLimit': 80, 'minChargeLimit': 20}, 'chargeState': {'batteryCapacity': None, 'batteryLevel': None, 'chargeLimit': None, 'chargeRate': None, 'chargeTimeRemaining': None, 'isCharging': False, 'isFullyCharged': None, 'isPluggedIn': False, 'lastUpdated': '2025-03-23T16:06:57.000Z', 'powerDeliveryState': 'UNPLUGGED', 'range': None}, 'id': 'cm3rogazq06pz13p8eucfutnx', 'information': {'brand': 'Wallbox', 'model': 'Pulsar Plus 1', 'year': None}, 'interventions': [], 'isReachable': True, 'lastSeen': '2025-03-23T16:24:51.913Z'}, {'canSmartCharge': True, 'chargeSettings': {'calculatedDeadline': '2025-03-24T06:00:00.000Z', 'capacity': 100, 'deadline': None, 'hourFriday': 420, 'hourMonday': 420, 'hourSaturday': 420, 'hourSunday': 420, 'hourThursday': 420, 'hourTuesday': 420, 'hourWednesday': 420, 'id': 'cm3rogap606pu13p8w08epzjx', 'initialCharge': 0, 'initialChargeTimestamp': '2024-11-21T19:00:15.016Z', 'isSmartChargingEnabled': True, 'isSolarChargingEnabled': False, 'maxChargeLimit': 80, 'minChargeLimit': 20}, 'chargeState': {'batteryCapacity': None, 'batteryLevel': None, 'chargeLimit': None, 'chargeRate': 10.71, 'chargeTimeRemaining': None, 'isCharging': True, 'isFullyCharged': None, 'isPluggedIn': True, 'lastUpdated': '2025-03-23T16:23:53.000Z', 'powerDeliveryState': 'PLUGGED_IN:CHARGING', 'range': None}, 'id': 'cm3rogap606pu13p8w08epzjx', 'information': {'brand': 'Wallbox', 'model': 'Pulsar Plus 2', 'year': None}, 'interventions': [], 'isReachable': True, 'lastSeen': '2025-03-23T16:24:50.746Z'}]}}
            if response is None:
                _LOGGER.debug("No response data for 'enodeChargers'")
                return {}
            if 'data' not in response:
                _LOGGER.debug("No data found in response for chargers: %s", response)
                return {}
            if response['data'] is None:
                _LOGGER.debug("No data for chargers found: %s", response)
                return {}   
            if 'enodeChargers' not in response['data']:
                _LOGGER.debug("No chargers found in data: %s", response)
                return {}   
            chargers_data = response.get("data", {}).get("enodeChargers", [])
            _LOGGER.info("%s Enode Chargers Found", len(chargers_data))
            _LOGGER.debug("Enode Chargers data: %s", chargers_data)
            # _LOGGER.debug("Format for 'enodeChargers' response: %s", type(response))
            # _LOGGER.debug("Format for 'enodeChargers' chargers: %s", type(chargers))
            # response is a disctionary, but the data is a list of dictionaries
            # chargers is a list of dictionaries, but the data is a dictionary
            # if not isinstance(chargers, list):
            #     _LOGGER.debug("Unexpected format for 'enodeChargers': %s", chargers)
            #     return []
            return EnodeChargers.from_dict(chargers_data)
        except Exception as error:
            _LOGGER.debug("Error in enode_chargers: %s", error)
            _LOGGER.exception("Unexpected error during query: %s", error)
            return {}
            # raise FrankEnergieException("Unexpected error occurred.") from error
#        except Exception as e:
#            raise FrankEnergieException(
#              f"Failed to fetch Enode Chargers: {e}"
#              ) from e


    async def invoices(self, site_reference: str) -> Invoices:
        """Retrieve the invoices data.

        Returns a Invoices object, containing the previous, current and upcoming invoice.
        """
        if self._auth is None or not self.is_authenticated:
            raise AuthRequiredException("Authentication is required.")

        query = FrankEnergieQuery(
            """
            query Invoices($siteReference: String!) {
                invoices(siteReference: $siteReference) {
                    allInvoices {
                        StartDate
                        PeriodDescription
                        TotalAmount
                        __typename
                    }
                    previousPeriodInvoice {
                        StartDate
                        PeriodDescription
                        TotalAmount
                        __typename
                    }
                    currentPeriodInvoice {
                        StartDate
                        PeriodDescription
                        TotalAmount
                        __typename
                    }
                    upcomingPeriodInvoice {
                        StartDate
                        PeriodDescription
                        TotalAmount
                        __typename
                    }
                __typename
                }
            __typename
            }
            """,
            "Invoices",
            {"siteReference": site_reference},
        )

        response = await self._query(query)
        return Invoices.from_dict(response)


    async def me(self, site_reference: str | None = None) -> Me:
        if self._auth is None:
            raise AuthRequiredException

        query = FrankEnergieQuery(
            """
            query Me($siteReference: String) {
                me {
                    ...UserFields
                }
            }
            fragment UserFields on User {
                id
                email
                countryCode
                advancedPaymentAmount(siteReference: $siteReference)
                treesCount
                hasInviteLink
                hasCO2Compensation
                createdAt
                updatedAt
                meterReadingExportPeriods(siteReference: $siteReference) {
                    EAN
                    cluster
                    segment
                    from
                    till
                    period
                    type
                }
                InviteLinkUser {
                    id
                    fromName
                    slug
                    treesAmountPerConnection
                    discountPerConnection
                }
                PushNotificationPriceAlerts {
                    id
                    isEnabled
                    type
                    weekdays
                }
                UserSettings {
                    id
                    disabledHapticFeedback
                    language
                    smartPushNotifications
                    rewardPayoutPreference
                }
                activePaymentAuthorization {
                    id
                    mandateId
                    signedAt
                    bankAccountNumber
                    status
                }
                meterReadingExportPeriods(siteReference: $siteReference) {
                    EAN
                    cluster
                    segment
                    from
                    till
                    period
                    type
                }
                connections(siteReference: $siteReference) {
                    id
                    connectionId
                    EAN
                    segment
                    status
                    contractStatus
                    estimatedFeedIn
                    firstMeterReadingDate
                    lastMeterReadingDate
                    meterType
                    externalDetails {
                        gridOperator
                        address {
                            street
                            houseNumber
                            houseNumberAddition
                            zipCode
                            city
                        }
                        contract {
                            startDate
                            endDate
                            contractType
                            productName
                            tariffChartId
                        }
                    }
                }
                externalDetails {
                    reference
                    person {
                        firstName
                        lastName
                    }
                    contact {
                        emailAddress
                        phoneNumber
                        mobileNumber
                    }
                    address {
                        addressFormatted
                        street
                        houseNumber
                        houseNumberAddition
                        zipCode
                        city
                    }
                    debtor {
                        bankAccountNumber
                        preferredAutomaticCollectionDay
                    }
                }
                smartCharging {
                    isActivated
                    provider
                    userCreatedAt
                    userId
                    isAvailableInCountry
                    needsSubscription
                    subscription {
                        startDate
                        endDate
                        id
                        proposition {
                            product
                            countryCode
                        }
                    }
                }
                smartTrading {
                    isActivated
                    isAvailableInCountry
                    userCreatedAt
                    userId
                }
                websiteUrl
                customerSupportEmail
                reference
            }
            """,
            "Me",
            {"siteReference": site_reference},
        )

        response = await self._query(query)
        return Me.from_dict(response)

    async def UserSites(self, site_reference: str | None = None) -> UserSites:
        if self._auth is None:
            raise AuthRequiredException

        query = FrankEnergieQuery(
            """
            query UserSites {
                userSites {
                    address {
                        addressFormatted
                    }
                    addressHasMultipleSites
                    deliveryEndDate
                    deliveryStartDate
                    firstMeterReadingDate
                    lastMeterReadingDate
                    propositionType
                    reference
                    segments
                    status
                }
            }
            """,
            "UserSites",
            {},
        )

        response = await self._query(query)
        return UserSites.from_dict(response)

    # query UserCountry {\\n  me {\\n    countryCode\\n  }\\n}\\n\",\"operationName\":\"UserCountry\"}
    # query UserSmartCharging {\\n  userSmartCharging {\\n    isActivated\\n    provider\\n    userCreatedAt\\n    userId\\n    isAvailableInCountry\\n    needsSubscription\\n    subscription {\\n      startDate\\n      endDate\\n      id\\n      proposition {\\n        product\\n        countryCode\\n      }\\n    }\\n  }\\n}\\n\",\"operationName\":\"UserSmartCharging\"}
    # {\"query\":\"query AppVersion {\\n  appVersion {\\n    ios {\\n      version\\n    }\\n    android {\\n      version\\n    }\\n  }\\n}\\n\",\"operationName\":\"AppVersion\"}"
    # \"query UserRewardsData {\\n  me {\\n    id\\n    UserSettings {\\n      id\\n      rewardPayoutPreference\\n    }\\n  }\\n  userRewardsData {\\n    activeConnectionsCount\\n    activeFriendsCount\\n    acceptedRewards {\\n      ...UserRewardV2Fields\\n    }\\n    upcomingRewards {\\n      ...UserRewardV2Fields\\n    }\\n  }\\n}\\n\\nfragment UserRewardV2Fields on UserRewardV2 {\\n  id\\n  awardedDiscount\\n  awardedTreesAmount\\n  availableForAcceptanceOn\\n  treesAmountPerConnection\\n  discountPerConnection\\n  acceptedOn\\n  isRewardForOwnSignup\\n  hasPossibleSmartChargingBonus\\n  coolingDownPeriod\\n  InviteLink {\\n    id\\n    type\\n    fromName\\n    templateType\\n    awardRewardType\\n    treesAmountPerConnection\\n    discountPerConnection\\n  }\\n  AdditionalBonuses {\\n    discountAmountPerConnection\\n    treesAmountPerConnection\\n    type\\n  }\\n}\\n\",\"operationName\":\"UserRewardsData\"}"
    # \"query TreeCertificates {\\n  treeCertificates {\\n    id\\n    imageUrl\\n    imagePath\\n    createdAt\\n    treesAmount\\n  }\\n}\\n\",\"operationName\":\"TreeCertificates\"}"
    # \"query AppNotice {\\n  appNotice {\\n    active\\n    message\\n    title\\n  }\\n}\\n\",\"operationName\":\"AppNotice\"}"

    async def user_country(self) -> Me:
        if self._auth is None:
            raise AuthRequiredException

        query = FrankEnergieQuery(
            """
            query UserCountry {
                me {
                    countryCode
                    }
            }
            """,
            "UserCountry",
            {}
        )

        response = await self._query(query)
        return Me.from_dict(response)

    async def user(self, site_reference: str | None = None) -> User:
        if self._auth is None:
            raise AuthRequiredException

        query = FrankEnergieQuery(
            """
            query Me($siteReference: String) {
                me {
                    ...UserFields
                }
            }
            fragment UserFields on User {
                id
                email
                countryCode
                advancedPaymentAmount(siteReference: $siteReference)
                treesCount
                hasInviteLink
                hasCO2Compensation
                createdAt
                updatedAt
                meterReadingExportPeriods(siteReference: $siteReference) {
                    EAN
                    cluster
                    segment
                    from
                    till
                    period
                    type
                }
                InviteLinkUser {
                    id
                    fromName
                    slug
                    treesAmountPerConnection
                    discountPerConnection
                }
                UserSettings {
                    id
                    disabledHapticFeedback
                    language
                    smartPushNotifications
                    rewardPayoutPreference
                }
                activePaymentAuthorization {
                    id
                    mandateId
                    signedAt
                    bankAccountNumber
                    status
                }
                meterReadingExportPeriods(siteReference: $siteReference) {
                    EAN
                    cluster
                    segment
                    from
                    till
                    period
                    type
                }
                connections(siteReference: $siteReference) {
                    id
                    connectionId
                    EAN
                    segment
                    status
                    contractStatus
                    estimatedFeedIn
                    firstMeterReadingDate
                    lastMeterReadingDate
                    meterType
                    externalDetails {
                        gridOperator
                        address {
                            street
                            houseNumber
                            houseNumberAddition
                            zipCode
                            city
                        }
                        contract {
                            startDate
                            endDate
                            contractType
                            productName
                            tariffChartId
                        }
                    }
                }
                externalDetails {
                    reference
                    person {
                        firstName
                        lastName
                    }
                    contact {
                        emailAddress
                        phoneNumber
                        mobileNumber
                    }
                    address {
                        street
                        houseNumber
                        houseNumberAddition
                        zipCode
                        city
                    }
                    debtor {
                        bankAccountNumber
                        preferredAutomaticCollectionDay
                    }
                }
                smartCharging {
                    isActivated
                    provider
                    userCreatedAt
                    userId
                    isAvailableInCountry
                    needsSubscription
                    subscription {
                        startDate
                        endDate
                        id
                        proposition {
                            product
                            countryCode
                        }
                    }
                }
                smartTrading {
                    isActivated
                    isAvailableInCountry
                    userCreatedAt
                    userId
                }
                websiteUrl
                customerSupportEmail
                reference
            }
            """,
            "Me",
            {"siteReference": site_reference},
        )
        
        response = await self._query(query)
        return User.from_dict(response)

    async def be_prices(
        self,
        start_date: Optional[date] | None = None,
        end_date: Optional[date] | None = None
    ) -> MarketPrices:
        """Get belgium market prices."""
        if start_date is None:
            start_date = datetime.now(timezone.utc).date()
        if end_date is None:
            end_date = start_date + timedelta(days=1)

        headers = {"x-country": "BE"}

        query = FrankEnergieQuery(
            """
            query MarketPrices ($date: String!) {
                marketPrices(date: $date) {
                    electricityPrices {
                        from
                        till
                        marketPrice
                        marketPriceTax
                        sourcingMarkupPrice
                        energyTaxPrice
                        perUnit
                        __typename
                    }
                    gasPrices {
                        from
                        till
                        marketPrice
                        marketPriceTax
                        sourcingMarkupPrice
                        energyTaxPrice
                        perUnit
                        __typename
                    }
                __typename
                }
            }
            """,
            "MarketPrices",
            {"date": str(start_date)},  
        )
        response = await self._query(query, extra_headers=headers)
        return MarketPrices.from_be_dict(response)

    async def prices(
        self, start_date: Optional[date] | None = None, end_date: Optional[date] | None = None
    ) -> MarketPrices:
        """Get market prices."""
        if not start_date:
            start_date = date.today()
        if not end_date:
            end_date = date.today() + timedelta(days=1)

        query = FrankEnergieQuery(
            """
            query MarketPrices($startDate: Date!, $endDate: Date!) {
                marketPricesElectricity(startDate: $startDate, endDate: $endDate) {
                    from
                    till
                    marketPrice
                    marketPriceTax
                    sourcingMarkupPrice
                    energyTaxPrice
                    perUnit
                    __typename
                }
                marketPricesGas(startDate: $startDate, endDate: $endDate) {
                    from
                    till
                    marketPrice
                    marketPriceTax
                    sourcingMarkupPrice
                    energyTaxPrice
                    perUnit
                    __typename
                }
                version
                __typename
            }
            """,
            "MarketPrices",
            {"startDate": str(start_date), "endDate": str(end_date)},
        )
        response = await self._query(query)
        return MarketPrices.from_dict(response)

    async def user_prices(
        self,
        site_reference: str,
        start_date: date,
        end_date: Optional[date] | None = None
    ) -> MarketPrices:
        """Get customer market prices."""
        if self._auth is None:
            raise AuthRequiredException

        if not start_date:
            start_date = date.today()
        if not end_date:
            end_date = date.today() + timedelta(days=1)

        query = FrankEnergieQuery(
            """
            query MarketPrices($date: String!, $siteReference: String!) {
                customerMarketPrices(date: $date, siteReference: $siteReference) {
                    id
                    averageElectricityPrices {
                        averageMarketPrice
                        averageMarketPricePlus
                        averageAllInPrice
                        perUnit
                        isWeighted
                    }
                    electricityPrices {
                        id
                        date
                        from
                        till
                        marketPrice
                        marketPricePlus
                        marketPriceTax
                        sourcingMarkupPrice: consumptionSourcingMarkupPrice
                        energyTaxPrice: energyTax
                        allInPrice
                        perUnit
                        allInPriceComponents {
                            name
                            value
                        }
                        marketPricePlusComponents {
                            name
                            value
                        }
                        __typename
                    }
                    gasPrices {
                        id
                        date
                        from
                        till
                        marketPrice
                        marketPricePlus
                        marketPriceTax
                        sourcingMarkupPrice: consumptionSourcingMarkupPrice
                        energyTaxPrice: energyTax
                        perUnit
                        allInPriceComponents {
                            name
                            value
                        }
                        marketPricePlusComponents {
                            name
                            value
                        }
                        __typename
                    }
                __typename
                }
            }
            """,
            "MarketPrices",
            {"date": str(start_date), "siteReference": site_reference},
        )
        response = await self._query(query)
        return MarketPrices.from_userprices_dict(response)

    async def period_usage_and_costs(self,
                                     site_reference: str,
                                     start_date: str,
                                     ) -> "PeriodUsageAndCosts":
        """
        Haalt het verbruik en de kosten op voor een specifieke periode en locatie.
        Dit is net als op de factuur de marktprijs+

        Args:
            site_reference (str): De referentie van de locatie.
            start_date (str | datetime.date): De startdatum van de periode waarvoor de gegevens moeten worden opgehaald.

        Returns:
            PeriodUsageAndCosts: Het verbruik en de kosten van gas, elektriciteit en teruglevering.

        Raises:
            AuthRequiredException: Als de authenticatie ontbreekt.
            FrankEnergieAPIException: Als de API een fout retourneert.
            ValueError: Als de site_reference leeg is of start_date in de toekomst ligt.
        """
        if not site_reference:
            raise ValueError("De 'site_reference' mag niet leeg zijn.")

        if self._auth is None:
            raise AuthRequiredException("Authenticatie is vereist om deze query uit te voeren.")

        query = FrankEnergieQuery(
            """
            query PeriodUsageAndCosts($date: String!, $siteReference: String!) {
                periodUsageAndCosts(date: $date, siteReference: $siteReference) {
                    _id
                    gas{
                        usageTotal
                        costsTotal
                        unit
                        items{
                            date
                            from
                            till
                            usage
                            costs
                            unit
                            __typename
                        }
                        __typename
                    }
                    electricity{
                        usageTotal
                        costsTotal
                        unit
                        items{
                            date
                            from
                            till
                            usage
                            costs
                            unit
                            __typename
                        }
                        __typename
                    }
                    feedIn {
                        usageTotal
                        costsTotal
                        unit
                        items {
                            date
                            from
                            till
                            usage
                            costs
                            unit
                            __typename
                        }
                        __typename
                    }
                    __typename
                }
                __typename
            }
            """,
            "PeriodUsageAndCosts",
            {
                "siteReference": site_reference,
                "date": str(start_date),
            },
        )

        try:
            response = await self._query(query)
            return PeriodUsageAndCosts.from_dict(response)
        except Exception as err:
            _LOGGER.exception("Fout bij ophalen van periodUsageAndCosts voor site %s op %s: %s",
                              site_reference, start_date, err)
            raise FrankEnergieException("Kon verbruik en kosten niet ophalen voor opgegeven periode.") from err


    async def smart_batteries(self) -> SmartBatteries | None:
        """Get the users smart batteries.
        For this to work, the user must have a smart battery connected to their account and smart-trading must be enabled.

        Returns a list of all smart batteries.
        """
        if self._auth is None:
            raise AuthRequiredException

        query = FrankEnergieQuery(
            """
            query SmartBatteries {
                smartBatteries {
                    brand
                    capacity
                    createdAt
                    externalReference
                    id
                    maxChargePower
                    maxDischargePower
                    provider
                    updatedAt
                    __typename
                }
            }
            """,
            "SmartBatteries",
        )

        try: 
            _LOGGER.debug("Querying smart batteries")
            response = await self._query(query)
        except Exception as e:
            _LOGGER.error("Failed to query smart batteries: %s", e)
            return None
    
        # Handle empty or missing response data
        if not response:
            _LOGGER.warning("Empty or missing GraphQL response for 'smartBatteries'")
            return None

        if response.get("errors"):
            _LOGGER.error("Error response for 'smartBatteries': %s", response)

        if not response.get("data"):
            _LOGGER.warning("Empty or missing GraphQL response for 'smartBatteries'")
            #return {}
            return None

        _LOGGER.debug("Response data for 'smartBatteries': %s", response)
        batteries_data = response.get("data", {}).get("smartBatteries")

        if not batteries_data:
            _LOGGER.debug("No smart batteries found")
            return SmartBatteries([])

        try:
            smart_batteries = [SmartBattery.from_dict(b) for b in batteries_data]
        except (KeyError, ValueError, TypeError) as err:
            _LOGGER.error("Failed to parse smart batteries: %s", err)
            return SmartBatteries([])

        return SmartBatteries(smart_batteries)


    async def smart_battery_details(self, device_id: str) -> SmartBatteryDetails | None:
        """Retrieve smart battery details and summary."""
        if self._auth is None:
            raise AuthRequiredException

        if not device_id:
            raise ValueError("Missing required device_id for smart_battery_sessions")

        query = FrankEnergieQuery(
            """
                query SmartBattery($deviceId: String!) {
                    smartBattery(deviceId: $deviceId) {
                        brand
                        capacity
                        id
                        settings {
                            batteryMode
                            imbalanceTradingStrategy
                            selfConsumptionTradingAllowed
                        }
                    }
                    smartBatterySummary(deviceId: $deviceId) {
                        lastKnownStateOfCharge
                        lastKnownStatus
                        lastUpdate
                        totalResult
                    }
                }
            """,
            "SmartBattery",
            {"deviceId": device_id}
        )

        try: 
            _LOGGER.debug("Querying smart battery details for device_id: %s", device_id)
            response = await self._query(query)
        except Exception as e:
            _LOGGER.error("Failed to query smart battery details: %s", e)
            return None

        if response is None:
            _LOGGER.debug("No response data for 'smartBatteries'")
            return None
        if "smartBattery" not in response["data"] or "smartBatterySummary" not in response["data"]:
            _LOGGER.debug("Incomplete response data for 'smartBattery' or 'smartBatterySummary'")
            return {}
        return {
            "smartBattery": SmartBattery.from_dict(response["data"]["smartBattery"]),
            "smartBatterySummary": SmartBatterySummary.from_dict(response["data"]["smartBatterySummary"]),
        }

    async def smart_battery_sessions(
        self, device_id: str, start_date: date, end_date: date
    ) -> SmartBatterySessions | None:
        """List smart battery sessions for a device.

        Returns a list of all smart battery sessions for a device.

        Full query:
        query SmartBatterySessions($startDate: String!, $endDate: String!, $deviceId: String!) {
            smartBatterySessions(
                startDate: $startDate
                endDate: $endDate
                deviceId: $deviceId
            ) {
                deviceId
                fairUsePolicyVerified
                periodEndDate
                periodEpexResult
                periodFrankSlim
                periodImbalanceResult
                periodStartDate
                periodTotalResult
                periodTradeIndex
                periodTradingResult
                sessions {
                    cumulativeTradingResult
                    cumulativeResult
                    date
                    tradingResult
                    result
                    status
                    tradeIndex
                }
                totalTradingResult
            }
        }
        """
        if self._auth is None:
            raise AuthRequiredException

        if not device_id:
            raise ValueError("Missing required device_id for smart_battery_sessions")

        query = FrankEnergieQuery(
            """
                query SmartBatterySessions($startDate: String!, $endDate: String!, $deviceId: String!) {
                    smartBatterySessions(
                        startDate: $startDate
                        endDate: $endDate
                        deviceId: $deviceId
                    ) {
                        deviceId
                        fairUsePolicyVerified
                        periodEndDate
                        periodEpexResult
                        periodFrankSlim
                        periodImbalanceResult
                        periodStartDate
                        periodTotalResult
                        periodTradeIndex
                        periodTradingResult
                        sessions {
                            cumulativeResult
                            date
                            result
                            status
                            tradeIndex
                        }
                    }
                    }
                """,
            "SmartBatterySessions",
            {
                "deviceId": device_id,
                "startDate": start_date.isoformat(),  # Ensures proper ISO 8601 format
                "endDate": end_date.isoformat(),      # Ensures proper ISO 8601 format
            },
        )

        try:
            _LOGGER.debug("Querying smart battery sessions for device_id: %s", device_id)
            response = await self._query(query)
            _LOGGER.debug("SmartBatterySessions Response: %s", response)
        except Exception as e:
            _LOGGER.error("Failed to query smart battery sessions: %s", e)
            return None

        return SmartBatterySessions.from_dict(response)

    ENODE_VEHICLES_QUERY = """
        query EnodeVehicles {
            enodeVehicles {
                canSmartCharge
                chargeSettings {
                    calculatedDeadline
                    deadline
                    hourFriday
                    hourMonday
                    hourSaturday
                    hourSunday
                    hourThursday
                    hourTuesday
                    hourWednesday
                    id
                    isSmartChargingEnabled
                    isSolarChargingEnabled
                    maxChargeLimit
                    minChargeLimit
                }
                chargeState {
                    batteryCapacity
                    batteryLevel
                    chargeLimit
                    chargeRate
                    chargeTimeRemaining
                    isCharging
                    isFullyCharged
                    isPluggedIn
                    lastUpdated
                    powerDeliveryState
                    range
                }
                id
                information {
                    brand
                    model
                    vin
                    year
                }
                interventions {
                    description
                    title
                }
                isReachable
                lastSeen
            }
        }
        """
    ENODE_VEHICLES_OPERATIONNAME = "EnodeVehicles"
    ENODE_VEHICLES_VARIABLES = {}

    async def enode_vehicles(self) -> EnodeVehicles | None:
        """Get the users enode vehicles.
        For this to work, the user must have a enode vehicle connected to their account and smart-trading must be enabled.

        Returns a list of all enode vehicles.
        """
        if self._auth is None:
            raise AuthRequiredException

        query = FrankEnergieQuery(
            self.ENODE_VEHICLES_QUERY,
            self.ENODE_VEHICLES_OPERATIONNAME,
            self.ENODE_VEHICLES_VARIABLES,
        )

        try: 
            _LOGGER.debug("Querying enode vehicles")
            response = await self._query(query)
            # return response["data"]["enodeVehicles"]
        except Exception as e:
            _LOGGER.error("Failed to query enode vehicles: %s", e)
            return None
    
        # Handle empty or missing response data
        if not response:
            _LOGGER.warning("Empty or missing GraphQL response for 'enodeVehicles'")
            return None

        if response.get("errors"):
            _LOGGER.error("Error response for 'enodeVehicles': %s", response)
            return None

        if not response.get("data"):
            _LOGGER.warning("Empty or missing GraphQL response for 'enodeVehicles'")
            #return {}
            return None

        _LOGGER.debug("Response data for 'enodeVehicles': %s", response)
        # vehicles_data = response.get("data", {}).get("enodeVehicles", {})
        vehicles_data = response["data"]["enodeVehicles"]

        if not vehicles_data:
            _LOGGER.debug("No enode vehicles found")
            return EnodeVehicles([])

        try:
            # enode_vehicles = [EnodeVehicles.from_dict(v) for v in vehicles_data]
            enode_vehicles = vehicles_data
        except (KeyError, ValueError, TypeError) as err:
            _LOGGER.error("Failed to parse enode vehicles: %s", err)
            return EnodeVehicles([])

        return EnodeVehicles(enode_vehicles)


    @property
    def is_authenticated(self) -> bool:
        """Check if the client is authenticated.

        Returns:
            True if the client is authenticated, False otherwise.

        Does not actually check if the token is valid.
        """
        return self._auth is not None and self._auth.authToken is not None

    def _validate_not_future_date(self, value: date) -> None:
        if value > datetime.now(timezone.utc).date():
            raise ValueError("De 'start_date' mag niet in de toekomst liggen.")

    def _validate_start_date_format(self, start_date: str | date) -> None:
        if isinstance(start_date, date):
            start_date = start_date.isoformat()

        if not re.fullmatch(r"\d{4}(-\d{2}){0,2}", start_date):
            raise ValueError("De 'start_date' moet een formaat hebben zoals 'YYYY', 'YYYY-MM' of 'YYYY-MM-DD'.")

        if len(start_date) == 10:  # volledige datum
            try:
                date_obj = datetime.strptime(start_date, "%Y-%m-%d").date()
                if date_obj > datetime.now(timezone.utc).date():
                    raise ValueError("De 'start_date' mag niet in de toekomst liggen.")
            except ValueError as e:
                raise ValueError("De 'start_date' heeft geen geldig datumformaat: %s" % e)

    async def close(self) -> None:
        """Close client session."""
        if self._close_session and self._session is not None:
            await self._session.close()
            self._session = None
            self._close_session = False

    async def __aenter__(self):
        """Async enter.

        Returns:
            The FrankEnergie object.
        """
        return self

    async def __aexit__(self, *_exc_info: Any) -> None:
        """Async exit.

        Args:
            _exc_info: Exec type.
        """
        await self.close()

    def introspect_schema(self):
        query = """
            query IntrospectionQuery {
                __schema {
                    types {
                        name
                        fields {
                            name
                        }
                    }
                }
            }
        """

        response = requests.post(self.DATA_URL, json={
                                 'query': query}, timeout=10)
        response.raise_for_status()
        result = response.json()
        return result

    def get_diagnostic_data(self):
        # Implement the logic to fetch diagnostic data from the FrankEnergie API
        # and return the data as needed for the diagnostic sensor
        return "Diagnostic data"


# frank_energie_instance = FrankEnergie()

# Call the introspect_schema method on the instance
# introspection_result = frank_energie_instance.introspect_schema()

# Print the result
# print("Introspection Result:", introspection_result)
