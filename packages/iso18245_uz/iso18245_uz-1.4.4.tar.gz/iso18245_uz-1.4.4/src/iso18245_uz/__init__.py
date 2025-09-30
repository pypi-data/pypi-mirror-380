import csv
from importlib.resources import files
from typing import Any, Dict, List, NamedTuple

ISO_VERSION_YEAR = 2003


class MCCNotFound(KeyError):
	pass


class InvalidMCC(ValueError):
	pass


class MCCRange(NamedTuple):
	start: str
	end: str
	description: str
	description_uz: str
	description_ru: str
	reserved: bool


class MCC(NamedTuple):
	mcc: str
	range: MCCRange
	iso_description: str
	iso_description_ru: str
	iso_description_uz: str
	usda_description: str
	usda_description_uz: str
	usda_description_ru: str
	stripe_description: str
	stripe_description_uz: str
	stripe_description_ru: str
	stripe_code: str
	visa_description: str
	visa_req_clearing_name: str
	visa_description_uz: str
	visa_description_ru: str
	alipay_description: str
	alipay_description_uz: str
	alipay_description_ru: str
	mastercard_description: str
	mastercard_abbreviated_airline_name: str
	mastercard_description_uz: str
	mastercard_description_ru: str
	amex_description: str
	amex_description_uz: str
	amex_description_ru: str


_cached_csv: Dict[str, List[List[str]]] = {}


def _load_csv(path: str) -> List[List[str]]:
	if path not in _cached_csv:
		ref = files("iso18245_uz") / "data" / path
		with ref.open("r") as f:
			reader = csv.reader(f)
			_cached_csv[path] = list(reader)[1:]

	return _cached_csv[path]


def _find_mcc_in_csv(mcc: str, path: str) -> List[str]:
	for row in _load_csv(path):
		if row[0] == mcc:
			return row[1:]
	return []


def validate_mcc(mcc: str) -> int:
	mcc_as_num = int(mcc)
	if mcc_as_num < 0 or mcc_as_num > 9999:
		raise InvalidMCC(mcc)

	return mcc_as_num


def get_mcc(mcc: str) -> MCC:
	mcc_range = get_mcc_range(mcc)
	found = False
	iso_description = ""
	iso_description_uz = ""
	iso_description_ru = ""
	usda_description = ""
	usda_description_uz = ""
	usda_description_ru = ""
	stripe_description = ""
	stripe_description_uz = ""
	stripe_description_ru = ""
	stripe_code = ""
	visa_description = ""
	visa_description_uz = ""
	visa_description_ru = ""
	visa_req_clearing_name = ""
	alipay_description = ""
	alipay_description_uz = ""
	alipay_description_ru = ""
	mastercard_description = ""
	mastercard_description_uz = ""
	mastercard_description_ru = ""
	mastercard_abbreviated_airline_name = ""
	amex_description = ""
	amex_description_uz = ""
	amex_description_ru = ""

	if not mcc_range.reserved:
		data = _find_mcc_in_csv(mcc, "iso18245_official_list_translated.csv")
		if data:
			iso_description, iso_description_uz, iso_description_ru, found = data[0], data[1], data[2], True

	usda_data = _find_mcc_in_csv(mcc, "usda_list_translated.csv")
	if usda_data:
		usda_description, usda_description_uz, usda_description_ru, found = usda_data[0], usda_data[1], usda_data[2], True

	visa_info = _find_mcc_in_csv(mcc, "visa_list_translated.csv")
	if visa_info:
		visa_description, visa_req_clearing_name, visa_description_uz, visa_description_ru, found = (
			visa_info[0],
			visa_info[1],
			visa_info[2],
			visa_info[3],
			True,
		)

	stripe_info = _find_mcc_in_csv(mcc, "stripe_list_translated.csv")
	if stripe_info:
		stripe_description, stripe_code, stripe_description_uz, stripe_description_ru, found = stripe_info[0], stripe_info[1], stripe_info[2], stripe_info[3], True

	alipay_info = _find_mcc_in_csv(mcc, "alipay_list_translated.csv")
	if alipay_info:
		alipay_description, alipay_description_uz, alipay_description_ru, found = alipay_info[0], alipay_info[1], alipay_info[2], True

	mastercard_info = _find_mcc_in_csv(mcc, "mastercard_list_translated.csv")
	if mastercard_info:
		mastercard_description, mastercard_abbreviated_airline_name, mastercard_description_uz, mastercard_description_ru, found = mastercard_info[0], mastercard_info[1], mastercard_info[2], mastercard_info[3], True

	amex_info = _find_mcc_in_csv(mcc, "amex_list_translated.csv")
	if amex_info:
		amex_description, amex_description_uz, amex_description_ru, found = amex_info[0], amex_info[1], amex_info[2], True

	if not found:
		raise MCCNotFound(mcc)

	return MCC(
		mcc=mcc,
		range=mcc_range,
		iso_description=iso_description,
		iso_description_ru=iso_description_ru,
		iso_description_uz=iso_description_uz,
		usda_description=usda_description,
		usda_description_uz=usda_description_uz,
		usda_description_ru=usda_description_ru,
		stripe_description=stripe_description,
		stripe_description_uz=stripe_description_uz,
		stripe_description_ru=stripe_description_ru,
		stripe_code=stripe_code,
		visa_description=visa_description,
		visa_req_clearing_name=visa_req_clearing_name,
		visa_description_uz=visa_description_uz,
		visa_description_ru=visa_description_ru,
		alipay_description=alipay_description,
		alipay_description_uz=alipay_description_uz,
		alipay_description_ru=alipay_description_ru,
		mastercard_description=mastercard_description,
		mastercard_description_uz=mastercard_description_uz,
		mastercard_description_ru=mastercard_description_ru,
		mastercard_abbreviated_airline_name=mastercard_abbreviated_airline_name,
		amex_description=amex_description,
		amex_description_uz=amex_description_uz,
		amex_description_ru=amex_description_ru,
	)


def get_mcc_range(mcc: str) -> MCCRange:
	mcc_as_num = validate_mcc(mcc)
	range_data = _load_csv("iso18245_ranges_translated.csv")
	for range_start, range_end, description, description_uz, description_ru in range_data:
		start_num, end_num = int(range_start), int(range_end)
		if start_num <= mcc_as_num <= end_num:
			return MCCRange(
				range_start,
				range_end,
				description,
				description_uz,
				description_ru,
				reserved=description.startswith("Reserved"),
			)

		if end_num > mcc_as_num:
			break

	raise RuntimeError(f"Could not find correct MCC range for {mcc} (likely a bug)")


def get_all_mccs_in_range(first: str, last: str) -> List[MCC]:
	first_num = validate_mcc(first)
	last_num = validate_mcc(last)

	lists = [
		_load_csv("iso18245_official_list_translated.csv"),
		_load_csv("stripe_list_translated.csv"),
		_load_csv("usda_list_translated.csv"),
		_load_csv("visa_list_translated.csv"),
		_load_csv("mastercard_list_translated.csv"),
		_load_csv("amex_list_translated.csv"),
	]

	mccs = set()

	for mcc_list in lists:
		for mcc in mcc_list:
			mcc_num = int(mcc[0])
			if mcc_num < first_num:
				continue
			elif mcc_num > last_num:
				break
			mccs.add(mcc[0])

	return [get_mcc(mcc) for mcc in sorted(mccs)]


def get_all_mccs() -> List[MCC]:
	return get_all_mccs_in_range("0000", "9999")


def get_all_mccs_dict() -> List[Dict[str, Any]]:
	"""Returns list of dictionaries for all MCCs, e.g. for easy conversion to pandas data frame using `DataFrame(get_all_mccs_dict())`."""
	return [{'mcc': item.mcc,\
			 'mcc_range_start': item.range.start,\
			 'mcc_range_end': item.range.end,\
			 'mcc_range_description': item.range.description,\
			 'mcc_range_reserved_flag': item.range.reserved,\
			 'iso_description': item.iso_description,\
			 'iso_description_uz': item.iso_description_uz,\
			 'iso_description_ru': item.iso_description_ru,\
			 'usda_description': item.usda_description,\
			 'usda_description_uz': item.usda_description_uz,\
			 'usda_description_ru': item.usda_description_ru,\
			 'stripe_description': item.stripe_description,\
			 'stripe_description_uz': item.stripe_description_uz,\
			 'stripe_description_ru': item.stripe_description_ru,\
			 'stripe_code': item.stripe_code,\
			 'visa_description': item.visa_description,\
			 'visa_req_clearing_name': item.visa_req_clearing_name,\
			 'visa_description_uz': item.visa_description_uz,\
			 'visa_description_ru': item.visa_description_ru,\
			 'alipay_description': item.alipay_description,\
			 'alipay_description_uz': item.alipay_description_uz,\
			 'alipay_description_ru': item.alipay_description_ru,\
			 'mastercard_description': item.mastercard_description,\
			 'mastercard_description_uz': item.mastercard_description_uz,\
			 'mastercard_description_ru': item.mastercard_description_ru,\
			 'mastercard_abbreviated_airline_name': item.mastercard_abbreviated_airline_name,\
			 'amex_description': item.amex_description,\
			 'amex_description_uz': item.amex_description_uz,\
			 'amex_description_ru': item.amex_description_ru,\
			} for item in get_all_mccs()]
