import voluptuous as vol
import homeassistant.helpers.config_validation as cv

DOMAIN = "octopus_energy"
INTEGRATION_VERSION = "12.0.2"

REFRESH_RATE_IN_MINUTES_ACCOUNT = 60
REFRESH_RATE_IN_MINUTES_INTELLIGENT = 5
REFRESH_RATE_IN_MINUTES_RATES = 15
REFRESH_RATE_IN_MINUTES_PREVIOUS_CONSUMPTION = 30
REFRESH_RATE_IN_MINUTES_STANDING_CHARGE = 60
REFRESH_RATE_IN_MINUTES_OCTOPLUS_SAVING_SESSIONS = 15
REFRESH_RATE_IN_MINUTES_OCTOPLUS_WHEEL_OF_FORTUNE = 60
REFRESH_RATE_IN_MINUTES_OCTOPLUS_POINTS = 60
REFRESH_RATE_IN_MINUTES_GREENNESS_FORECAST = 180
REFRESH_RATE_IN_MINUTES_HOME_PRO_CONSUMPTION = 0.17

CONFIG_VERSION = 4

CONFIG_KIND = "kind"
CONFIG_KIND_ACCOUNT = "account"
CONFIG_KIND_TARGET_RATE = "target_rate"
CONFIG_KIND_COST_TRACKER = "cost_tracker"
CONFIG_KIND_TARIFF_COMPARISON = "tariff_comparison"

CONFIG_MAIN_OLD_API_KEY = "Api key"
CONFIG_MAIN_OLD_ACCOUNT_ID = "Account Id"

CONFIG_MAIN_API_KEY = "api_key"
CONFIG_ACCOUNT_ID = "account_id"
CONFIG_MAIN_SUPPORTS_LIVE_CONSUMPTION = "supports_live_consumption"
CONFIG_MAIN_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES = "live_electricity_consumption_refresh_in_minutes"
CONFIG_MAIN_LIVE_GAS_CONSUMPTION_REFRESH_IN_MINUTES = "live_gas_consumption_refresh_in_minutes"
CONFIG_MAIN_CALORIFIC_VALUE = "calorific_value"
CONFIG_MAIN_PREVIOUS_ELECTRICITY_CONSUMPTION_DAYS_OFFSET = "previous_electricity_consumption_days_offset"
CONFIG_MAIN_PREVIOUS_GAS_CONSUMPTION_DAYS_OFFSET = "previous_gas_consumption_days_offset"
CONFIG_MAIN_ELECTRICITY_PRICE_CAP = "electricity_price_cap"
CONFIG_MAIN_GAS_PRICE_CAP = "gas_price_cap"
CONFIG_MAIN_HOME_PRO_ADDRESS = "home_pro_address"
CONFIG_MAIN_HOME_PRO_API_KEY = "home_pro_api_key"
CONFIG_FAVOUR_DIRECT_DEBIT_RATES = "favour_direct_debit_rates"

CONFIG_DEFAULT_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES = 1
CONFIG_DEFAULT_LIVE_GAS_CONSUMPTION_REFRESH_IN_MINUTES = 2
CONFIG_DEFAULT_PREVIOUS_CONSUMPTION_OFFSET_IN_DAYS = 1

CONFIG_TARGET_OLD_NAME = "Name"
CONFIG_TARGET_OLD_HOURS = "Hours"
CONFIG_TARGET_OLD_TYPE = "Type"
CONFIG_TARGET_OLD_START_TIME = "Start time"
CONFIG_TARGET_OLD_END_TIME = "End time"
CONFIG_TARGET_OLD_MPAN = "MPAN"

CONFIG_TARGET_NAME = "name"
CONFIG_TARGET_HOURS = "hours"
CONFIG_TARGET_HOURS_MODE = "hours_mode"
CONFIG_TARGET_HOURS_MODE_EXACT = "exact_hours"
CONFIG_TARGET_HOURS_MODE_MINIMUM = "minimum_hours"
CONFIG_TARGET_HOURS_MODE_MAXIMUM = "maximum_hours"
CONFIG_TARGET_TYPE = "type"
CONFIG_TARGET_TYPE_CONTINUOUS = "Continuous"
CONFIG_TARGET_TYPE_INTERMITTENT = "Intermittent"
CONFIG_TARGET_START_TIME = "start_time"
CONFIG_TARGET_END_TIME = "end_time"
CONFIG_TARGET_MPAN = "mpan"
CONFIG_TARGET_OFFSET = "offset"
CONFIG_TARGET_ROLLING_TARGET = "rolling_target"
CONFIG_TARGET_LAST_RATES = "last_rates"
CONFIG_TARGET_INVERT_TARGET_RATES = "target_invert_target_rates"
CONFIG_TARGET_MIN_RATE = "minimum_rate"
CONFIG_TARGET_MAX_RATE = "maximum_rate"
CONFIG_TARGET_WEIGHTING = "weighting"

CONFIG_TARGET_KEYS = [
  CONFIG_TARGET_NAME,
  CONFIG_TARGET_HOURS,
  CONFIG_TARGET_TYPE,
  CONFIG_TARGET_START_TIME,
  CONFIG_TARGET_END_TIME,
  CONFIG_TARGET_MPAN,
  CONFIG_TARGET_OFFSET,
  CONFIG_TARGET_ROLLING_TARGET,
  CONFIG_TARGET_LAST_RATES,
  CONFIG_TARGET_INVERT_TARGET_RATES,
  CONFIG_TARGET_MIN_RATE,
  CONFIG_TARGET_MAX_RATE,
  CONFIG_TARGET_WEIGHTING
]

CONFIG_COST_TRACKER_NAME = "name"
CONFIG_COST_TRACKER_MPAN = "mpan"
CONFIG_COST_TRACKER_TARGET_ENTITY_ID = "target_entity_id"
CONFIG_COST_TRACKER_ENTITY_ACCUMULATIVE_VALUE = "entity_accumulative_value"
CONFIG_COST_TRACKER_WEEKDAY_RESET = "weekday_reset"
CONFIG_COST_TRACKER_MONTH_DAY_RESET = "month_day_reset"

CONFIG_TARIFF_COMPARISON_NAME = "name"
CONFIG_TARIFF_COMPARISON_MPAN_MPRN = "mpan_mprn"
CONFIG_TARIFF_COMPARISON_PRODUCT_CODE = "product_code"
CONFIG_TARIFF_COMPARISON_TARIFF_CODE = "tariff_code"

DATA_CONFIG = "CONFIG"
DATA_ELECTRICITY_RATES_COORDINATOR_KEY = "ELECTRICITY_RATES_COORDINATOR_{}_{}"
DATA_ELECTRICITY_RATES_KEY = "ELECTRICITY_RATES_{}_{}"
DATA_CLIENT = "CLIENT"
DATA_HOME_PRO_CLIENT = "HOME_PRO_CLIENT"
DATA_GAS_TARIFF_CODE = "GAS_TARIFF_CODE"
DATA_ACCOUNT = "ACCOUNT"
DATA_ACCOUNT_COORDINATOR = "ACCOUNT_COORDINATOR"
DATA_SAVING_SESSIONS = "SAVING_SESSIONS"
DATA_SAVING_SESSIONS_COORDINATOR = "SAVING_SESSIONS_COORDINATOR"
DATA_KNOWN_TARIFF = "KNOWN_TARIFF"
DATA_GAS_RATES_COORDINATOR_KEY = "DATA_GAS_RATES_COORDINATOR_{}_{}"
DATA_GAS_RATES_KEY = "GAS_RATES_{}_{}"
DATA_INTELLIGENT_DEVICE = "INTELLIGENT_DEVICE"
DATA_INTELLIGENT_MPAN = "INTELLIGENT_MPAN"
DATA_INTELLIGENT_SERIAL_NUMBER = "INTELLIGENT_SERIAL_NUMBER"
DATA_INTELLIGENT_DISPATCHES = "INTELLIGENT_DISPATCHES"
DATA_INTELLIGENT_DISPATCHES_COORDINATOR = "INTELLIGENT_DISPATCHES_COORDINATOR"
DATA_INTELLIGENT_SETTINGS = "INTELLIGENT_SETTINGS"
DATA_INTELLIGENT_SETTINGS_COORDINATOR = "INTELLIGENT_SETTINGS_COORDINATOR"
DATA_ELECTRICITY_STANDING_CHARGE_KEY = "ELECTRICITY_STANDING_CHARGES_{}_{}"
DATA_GAS_STANDING_CHARGE_KEY = "GAS_STANDING_CHARGES_{}_{}"
DATA_WHEEL_OF_FORTUNE_SPINS = "WHEEL_OF_FORTUNE_SPINS"
DATA_CURRENT_CONSUMPTION_KEY = "CURRENT_CONSUMPTION_{}"
DATA_GREENNESS_FORECAST_COORDINATOR = "GREENNESS_FORECAST_COORDINATOR"
DATA_GREENNESS_FORECAST = "GREENNESS_FORECAST"
DATA_PREVIOUS_CONSUMPTION_COORDINATOR_KEY = "DATA_PREVIOUS_CONSUMPTION_AND_COST_COORDINATOR_{}_{}"
DATA_HOME_PRO_CURRENT_CONSUMPTION_KEY = "HOME_PRO_CURRENT_CONSUMPTION_{}"

DATA_SAVING_SESSIONS_FORCE_UPDATE = "SAVING_SESSIONS_FORCE_UPDATE"

STORAGE_COMPLETED_DISPATCHES_NAME = "octopus_energy.{}-completed-intelligent-dispatches.json"
STORAGE_ELECTRICITY_TARIFF_OVERRIDE_NAME = "octopus_energy.{}-{}-tariff-override.json"
STORAGE_TARIFF_CACHE_NAME = "octopus_energy.tariff-{}.json"

INTELLIGENT_SOURCE_SMART_CHARGE = "smart-charge"
INTELLIGENT_SOURCE_BUMP_CHARGE = "bump-charge"

REGEX_HOURS = "^[0-9]+(\\.[0-9]+)*$"
REGEX_TIME = "^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$"
REGEX_ENTITY_NAME = "^[a-z0-9_]+$"
# According to https://www.guylipman.com/octopus/api_guide.html#s1b, this part should indicate the types of tariff
# However it looks like there are some tariffs that don't fit this mold
REGEX_TARIFF_PARTS = "^((?P<energy>[A-Z])-(?P<rate>[0-9A-Z]+)-)?(?P<product_code>[A-Z0-9-]+)-(?P<region>[A-Z])$"
REGEX_OFFSET_PARTS = "^(-)?([0-1]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$"
REGEX_DATE = "^[0-9]{4}-[0-9]{2}-[0-9]{2}$"
REGEX_PRICE = "^(-)?[0-9]+(\\.[0-9]+)*$"

REGEX_WEIGHTING_NUMBERS = "([0-9](,[0-9]+)*)"
REGEX_WEIGHTING_START = "(\\*(,[0-9]+)+)"
REGEX_WEIGHTING_MIDDLE = "([0-9](,[0-9]+)*(,\\*)(,[0-9]+)+)"
REGEX_WEIGHTING_END = "([0-9](,[0-9]+)*(,\\*))"
REGEX_WEIGHTING = f"^({REGEX_WEIGHTING_NUMBERS}|{REGEX_WEIGHTING_START}|{REGEX_WEIGHTING_MIDDLE}|{REGEX_WEIGHTING_END})$"

DEFAULT_CALORIFIC_VALUE = 40.0

DATA_SCHEMA_ACCOUNT = vol.Schema({
  vol.Required(CONFIG_ACCOUNT_ID): str,
  vol.Required(CONFIG_MAIN_API_KEY): str,
  vol.Required(CONFIG_MAIN_PREVIOUS_ELECTRICITY_CONSUMPTION_DAYS_OFFSET, default=CONFIG_DEFAULT_PREVIOUS_CONSUMPTION_OFFSET_IN_DAYS): cv.positive_int,
  vol.Required(CONFIG_MAIN_PREVIOUS_GAS_CONSUMPTION_DAYS_OFFSET, default=CONFIG_DEFAULT_PREVIOUS_CONSUMPTION_OFFSET_IN_DAYS): cv.positive_int,
  vol.Required(CONFIG_MAIN_CALORIFIC_VALUE, default=DEFAULT_CALORIFIC_VALUE): cv.positive_float,
  vol.Required(CONFIG_MAIN_SUPPORTS_LIVE_CONSUMPTION): bool,
  vol.Optional(CONFIG_MAIN_HOME_PRO_ADDRESS): str,
  vol.Optional(CONFIG_MAIN_HOME_PRO_API_KEY): str,
  vol.Required(CONFIG_MAIN_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES, default=CONFIG_DEFAULT_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES): cv.positive_int,
  vol.Required(CONFIG_MAIN_LIVE_GAS_CONSUMPTION_REFRESH_IN_MINUTES, default=CONFIG_DEFAULT_LIVE_ELECTRICITY_CONSUMPTION_REFRESH_IN_MINUTES): cv.positive_int,
  vol.Optional(CONFIG_MAIN_ELECTRICITY_PRICE_CAP): cv.positive_float,
  vol.Optional(CONFIG_MAIN_GAS_PRICE_CAP): cv.positive_float,
  vol.Required(CONFIG_FAVOUR_DIRECT_DEBIT_RATES): bool
})

EVENT_ELECTRICITY_PREVIOUS_DAY_RATES = "octopus_energy_electricity_previous_day_rates"
EVENT_ELECTRICITY_CURRENT_DAY_RATES = "octopus_energy_electricity_current_day_rates"
EVENT_ELECTRICITY_NEXT_DAY_RATES = "octopus_energy_electricity_next_day_rates"
EVENT_ELECTRICITY_PREVIOUS_CONSUMPTION_RATES = "octopus_energy_electricity_previous_consumption_rates"
EVENT_ELECTRICITY_PREVIOUS_CONSUMPTION_OVERRIDE_RATES = "octopus_energy_electricity_previous_consumption_override_rates"
EVENT_ELECTRICITY_PREVIOUS_CONSUMPTION_TARIFF_COMPARISON_RATES = "octopus_energy_elec_previous_consumption_tariff_comparison_rates"

EVENT_GAS_PREVIOUS_DAY_RATES = "octopus_energy_gas_previous_day_rates"
EVENT_GAS_CURRENT_DAY_RATES = "octopus_energy_gas_current_day_rates"
EVENT_GAS_NEXT_DAY_RATES = "octopus_energy_gas_next_day_rates"
EVENT_GAS_PREVIOUS_CONSUMPTION_RATES = "octopus_energy_gas_previous_consumption_rates"
EVENT_GAS_PREVIOUS_CONSUMPTION_OVERRIDE_RATES = "octopus_energy_gas_previous_consumption_override_rates"
EVENT_GAS_PREVIOUS_CONSUMPTION_TARIFF_COMPARISON_RATES = "octopus_energy_gas_previous_consumption_tariff_comparison_rates"

EVENT_NEW_SAVING_SESSION = "octopus_energy_new_octoplus_saving_session"
EVENT_ALL_SAVING_SESSIONS = "octopus_energy_all_octoplus_saving_sessions"

REPAIR_UNIQUE_RATES_CHANGED_KEY = "electricity_unique_rates_updated_{}"
REPAIR_INVALID_API_KEY = "invalid_api_key_{}"
REPAIR_ACCOUNT_NOT_FOUND = "account_not_found_{}"

# During BST, two records are returned before the rest of the data is available
MINIMUM_CONSUMPTION_DATA_LENGTH = 3

COORDINATOR_REFRESH_IN_SECONDS = 60
HOME_PRO_COORDINATOR_REFRESH_IN_SECONDS = 10