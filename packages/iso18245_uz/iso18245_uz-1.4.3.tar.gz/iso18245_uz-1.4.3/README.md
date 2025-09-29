# python-iso18245-uz

A Python implementation of the ISO 18245 Merchant Category Codes database. This is fork package, mcc descriptions translated to Uzbek and Russian Languages using googletranslate. For Original repo please refer to [https://github.com/jleclanche/python-iso18245](https://github.com/jleclanche/python-iso18245).

## Installation

- `pip install iso18245_uz`

## Usage

```py

>>> import iso18245_uz
>>> iso18245_uz.get_mcc("5542")
MCC(mcc='5542', range=MCCRange(start='5000', end='5599', description='Retail outlets', description_uz="Chakana savdo do'konlari", description_ru='Розничные торговые точки', reserved=False), iso_description='Automated fuel dispensers', iso_description_ru='Автоматизированный топливный дозаторы', iso_description_uz="Avtomatlashtirilgan yonilg'i quyish vositalari", usda_description='Automated Fuel Dispensers', usda_description_uz="Avtomatlashtirilgan yonilg'i quyish vositalari", usda_description_ru='Автоматизированный топливный дозаторы', stripe_description='Automated Fuel Dispensers', stripe_description_uz="Avtomatlashtirilgan yonilg'i quyish vositalari", stripe_description_ru='Автоматизированный топливный дозаторы', stripe_code='automated_fuel_dispensers', visa_description='Automated Fuel Dispensers', visa_req_clearing_name='', visa_description_uz="Avtomatlashtirilgan yonilg'i quyish vositalari", visa_description_ru='Автоматизированный топливный дозаторы', alipay_description='Automated fuel dispensers', alipay_description_uz="Avtomatlashtirilgan yonilg'i quyish vositalari", alipay_description_ru='Автоматизированный топливный дозаторы', mastercard_description='Fuel Dispenser, Automated', mastercard_abbreviated_airline_name='', mastercard_description_uz="Yoqilg'i dispenseri, avtomatlashtirilgan", mastercard_description_ru='Топливный диспенсер, автоматизированный', amex_description='Automated Fuel Dispensers', amex_description_uz="Avtomatlashtirilgan yonilg'i quyish vositalari", amex_description_ru='Автоматизированный топливный дозаторы')
>>> iso18245_uz.get_mcc("3000")
MCC(mcc='3000', range=MCCRange(start='3000', end='3999', description='Reserved for private use', description_uz='Xususiy foydalanish uchun ajratilgan', description_ru='Зарезервировано для частного использования', reserved=True), iso_description='', iso_description_ru='', iso_description_uz='', usda_description='UNITED AIRLINES', usda_description_uz='Yagona Airlines', usda_description_ru='United Airlines', stripe_description='', stripe_description_uz='', stripe_description_ru='', stripe_code='', visa_description='UNITED AIRLINES', visa_req_clearing_name='UNITED AIR', visa_description_uz='Yagona Airlines', visa_description_ru='United Airlines', alipay_description='', alipay_description_uz='', alipay_description_ru='', mastercard_description='United Airlines', mastercard_abbreviated_airline_name='UNITED', mastercard_description_uz='Yagona Airlines', mastercard_description_ru='United Airlines', amex_description='UNITED AIRLINES', amex_description_uz='Yagona Airlines', amex_description_ru='United Airlines')>>> iso18245.get_mcc("3000").usda_description
'UNITED AIRLINES'
>>> iso18245_uz.get_mcc("3000").range
MCCRange(start='3000', end='3999', description='Reserved for private use', description_uz='Xususiy foydalanish uchun ajratilgan', description_ru='Зарезервировано для частного использования', reserved=True)
>>> iso18245_uz.get_mcc("999999")
Traceback (most recent call last):
  …
iso18245_uz.InvalidMCC: 999999
```

## External links

- [Wikipedia: ISO 18245](https://en.wikipedia.org/wiki/ISO_18245)
- [ISO Standard 18245:2023](https://www.iso.org/standard/79450.html)
- [AFNOR: ISO 18245](http://portailgroupe.afnor.fr/public_espacenormalisation/ISOTC68SC7/ISO%2018245.html)
- [Stripe MCC List](https://stripe.com/docs/issuing/categories)
- [USDA MCC List (incl. private MCCs)](https://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)
- [VISA Merchant Data Standards Manual](https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf) ([archived](https://web.archive.org/web/20240409085635/https://usa.visa.com/content/dam/VCOM/download/merchants/visa-merchant-data-standards-manual.pdf))
- [Mastercard Quick Reference Booklet](https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/quick-reference-booklet-merchant.pdf) ([archived](https://web.archive.org/web/20240419100915/https://www.mastercard.us/content/dam/public/mastercardcom/na/global-site/documents/quick-reference-booklet-merchant.pdf))
- [American Express Global Codes & Information Guide](https://www.americanexpress.com/content/dam/amex/us/merchant/new-merchant-specifications/GlobalCodesInfo_FINAL.pdf) ([archived](https://web.archive.org/web/20240419101013/https://www.americanexpress.com/content/dam/amex/us/merchant/new-merchant-specifications/GlobalCodesInfo_FINAL.pdf))

## Reference

This package is a fork of the original [python-iso18245](https://github.com/jleclanche/python-iso18245) by Jerome Leclanche, with MCC descriptions translated to Uzbek and Russian languages using Google Translate.

### Original Package

- **Repository**: https://github.com/jleclanche/python-iso18245
- **Author**: Jerome Leclanche
- **License**: MIT

### Translation Credits

- Russian and Uzbek translations were generated using Google Translate
- Original English descriptions remain available in the data structure
