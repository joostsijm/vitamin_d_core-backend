# # to run the app type:
# # set FLASK_APP=main.py
# # flask run
# # in the terminal
#
#
# from flask import Flask, request, redirect, url_for
# from flask_mongoengine import MongoEngine
# from DatabaseClasses import *
#
#
# class Config(object):
#     MONGODB_SETTINGS = {'db': 'IoTVitamineD'}
#
#
# db = MongoEngine()
#
# app = Flask(__name__)
# app.config.from_object(Config)
# db.init_app(app)
#
#
# @app.route('/n')
# def home():
#     return "hallo"
#
#
# @app.route('/sendName/<geslacht>/<voornaam>/<initialen>/<roepnaam>/<straatnaam>/<huisnr>/<huisnrletter>/<huisnrtvg>/'
#            '<aanduidingnr>/<woonplaats>/<gemeente>/<land>/<postcode>/<aditineleinfo>/<adresssoort>/<voorvoegsel>/'
#            '<achternaam>/<telefoonnr>/<toelichting>/<telecom>/<nrsoort>/<emailadr>/<emailsoort>')
# def sendName(geslacht, voornaam, initialen, roepnaam, straatnaam, huisnr, huisnrletter, huisnrtvg, aanduidingnr,
#              woonplaats, gemeente, land, postcode, aditineleinfo, adresssoort, voorvoegsel, achternaam, telefoonnr,
#              toelichting, telecom, nrsoort, emailadr, emailsoort):
#     user = User(geslacht=geslacht)
#     user.naamgegevens = NaamgegevensUser(voornamen=voornaam, initialen=initialen,
#                                          roepnaam=roepnaam)
#     user.naamgegevens.adressgegevens = AdressgegevensUser(straat=straatnaam,
#                                                           huisnummer=huisnr, huisnummerletter=huisnrletter,
#                                                           huisnummerToevoeging=huisnrtvg,
#                                                           aanduidingBijNummer=aanduidingnr, woonplaats=woonplaats,
#                                                           gemeente=gemeente,
#                                                           land=land, postcode=postcode,
#                                                           aditioneleInformatie=aditineleinfo,
#                                                           adressSoort=adresssoort)
#     user.naamgegevens.geslachtsnaam = GeslachtsnaamUser(voorvoegsels=voorvoegsel, achternaam=achternaam)
#     user.naamgegevens.contactgegevens = ContactgegevensUser()
#     user.naamgegevens.contactgegevens.telefoonnummer = TelefoonnummersUser(telefoonnummer=telefoonnr,
#                                                                            toelichting=toelichting,
#                                                                            telecomType=telecom,
#                                                                            nummerSoort=nrsoort)
#     user.naamgegevens.contactgegevens.emailAdressen = EmailAdressenUser(emailAdres=emailadr,
#                                                                         emailSoort=emailsoort)
#     user.save()
#     return 'send'
#
# @app.route('/getdata/<voornaam>/<achternaam>')
# def getdata(voornaam, achternaam):
#
#     if (voornaam & achternaam) != ' ':
#         get_data = User.objects(naamgegevens__voornamen=voornaam, naamgegevens__geslachtsnaam__achternaam=achternaam)
#     elif voornaam != ' ':
#         get_data = User.objects(naamgegevens__voornamen=voornaam)
#     elif achternaam != ' ':
#         get_data = User.objects(naamgegevens__geslachtsnaam__achternaam=achternaam)
#     else:
#         get_data = User.objects()
#
#     return jsonify(get_data)
#
#
#
# @app.route('/core', methods=['POST'])
# def login():
#     action = request.form['action']
#     req_geslacht = request.form['geslacht']
#     req_voornaam = request.form['voornaam']
#     req_initialen = request.form['initialen']
#     req_roepnaam = request.form['roepnaam']
#     req_straatnaam = request.form['straatnaam']
#     req_huisnr = request.form['huisnr']
#     req_huisnrletter = request.form['huisnrletter']
#     req_huisnrtvg = request.form['huisnrtvg']
#     req_aanduidingnr = request.form['aanduidingnr']
#     req_woonplaats = request.form['woonplaats']
#     req_gemeente = request.form['gemeente']
#     req_land = request.form['land']
#     req_postcode = request.form['postcode']
#     req_aditineleinfo = request.form['aditineleinfo']
#     req_adresssoort = request.form['adresssoort']
#     req_voorvoegsel = request.form['voorvoegsel']
#     req_achternaam = request.form['achternaam']
#     req_telefoonnr = request.form['telefoonnr']
#     req_toelichting = request.form['toelichting']
#     req_telecom = request.form['telecom']
#     req_nrsoort = request.form['nrsoort']
#     req_emailadr = request.form['emailadr']
#     req_emailsoort = request.form['emailsoort']
#
#     if action == 'send':
#         return redirect(url_for('sendName', geslacht=req_geslacht, voornaam=req_voornaam, initialen=req_initialen,
#                                 roepnaam=req_roepnaam, straatnaam=req_straatnaam, huisnr=req_huisnr,
#                                 huisnrletter=req_huisnrletter, huisnrtvg=req_huisnrtvg, aanduidingnr=req_aanduidingnr,
#                                 woonplaats=req_woonplaats, gemeente=req_gemeente, land=req_land, postcode=req_postcode,
#                                 aditineleinfo=req_aditineleinfo, adresssoort=req_adresssoort,
#                                 voorvoegsel=req_voorvoegsel, achternaam=req_achternaam, telefoonnr=req_telefoonnr,
#                                 toelichting=req_toelichting, telecom=req_telecom, nrsoort=req_nrsoort,
#                                 emailadr=req_emailadr, emailsoort=req_emailsoort))
#     elif action == 'replace':
#         return redirect(url_for('getdata'))
#
#     elif action == 'get':
#         return User