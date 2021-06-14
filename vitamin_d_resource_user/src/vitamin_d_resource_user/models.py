"""Database models"""

from flask_mongoengine import mongoengine as me

TELECOMTYPE = ('LL', 'FAX', 'MC', 'PG')
NUMMERSOORT = ('HP', 'TMP', 'WP')
EMAILSOORT = ('HP', 'WP')
LANDSOORT = ('6030', 'NL')
ADRESSSOORT = ('PST', 'HP', 'PHYS', 'TMP', 'WP', 'HV')
GESLACHTSSOORT = ('UN', 'M', 'F', 'UNK')
ZORGVERLENERROL = ('RESP', 'REF', 'PRF', 'SPRF', 'CON', 'ATND', 'OTH')
KLEDINGKEUZE = ('UNDRESSED', 'MINIMAL', 'FULL', 'DIAPER')
POSITIEKEUZE = ('staande positie', 'liggende positie')


class TelefoonnummersUser(me.EmbeddedDocument):
    telefoonnummer = me.IntField()
    toelichting = me.StringField()
    telecomType = me.StringField(choices=TELECOMTYPE)   #'LL', 'FAX', 'MC', 'PG'
    nummerSoort = me.StringField(choices=NUMMERSOORT)   #'HP', 'TMP', 'WP'


class EmailAdressenUser(me.EmbeddedDocument):
    emailAdres = me.EmailField()
    emailSoort = me.StringField(choices=EMAILSOORT)     #'HP', 'WP'


class ContactgegevensUser(me.EmbeddedDocument):
    telefoonnummer = me.EmbeddedDocumentField(TelefoonnummersUser)
    emailAdressen = me.EmbeddedDocumentField(EmailAdressenUser)


class AdressgegevensUser(me.EmbeddedDocument):
    straat = me.StringField()
    huisnummer = me.IntField()
    huisnummerletter = me.StringField()
    huisnummerToevoeging = me.StringField()
    aanduidingBijNummer = me.StringField()
    woonplaats = me.StringField()
    gemeente = me.StringField()
    land = me.StringField(choices=LANDSOORT)            #'6030', 'NL'
    postcode = me.StringField()
    aditioneleInformatie = me.StringField()
    adressSoort = me.StringField(choices=ADRESSSOORT)   #'PST', 'HP', 'PHYS', 'TMP', 'WP', 'HV'


class GeslachtsnaamUser(me.EmbeddedDocument):
    voorvoegsels = me.StringField()
    achternaam = me.StringField()


class NaamgegevensUser(me.EmbeddedDocument):
    naamgegevens_id = me.IntField()
    titels = me.StringField()
    voornamen = me.StringField()
    initialen = me.StringField()
    roepnaam = me.StringField()
    adressgegevens = me.EmbeddedDocumentField(AdressgegevensUser)
    geslachtsnaam = me.EmbeddedDocumentField(GeslachtsnaamUser)
    contactgegevens = me.EmbeddedDocumentField(ContactgegevensUser)


class Administrator(me.Document):
    administrator_id = me.IntField()
    geboortedatum = me.DateTimeField()
    geslacht = me.StringField(choices=GESLACHTSSOORT)           #'UN', 'M', 'F', 'UNK'
    specialisme = me.StringField()
    zorgverlenerRol = me.StringField(choices=ZORGVERLENERROL)   #'RESP', 'REF', 'PRF', 'SPRF', 'CON', 'ATND', 'OTH'
    naamgegevens = me.EmbeddedDocumentField(NaamgegevensUser)
    username = me.EmailField()
    password = me.StringField()


class Lichaamsgewicht(me.EmbeddedDocument):
    gewichtWaarde = me.IntField()
    gewichtDatum = me.DateTimeField()
    toelichting = me.StringField()
    kleding = me.StringField(choices=KLEDINGKEUZE)      #'UNDRESSED', 'MINIMAL', 'FULL', 'DIAPER'


class Lichaamslengte(me.EmbeddedDocument):
    lengteWaarde = me.IntField()
    lengteDatum = me.DateTimeField()
    toelichting = me.StringField()
    positie = me.StringField(choices=POSITIEKEUZE)      #'staande positie', 'liggende positie'


class UserData(me.EmbeddedDocument):
    lichaamsgewicht = me.EmbeddedDocumentField(Lichaamsgewicht)
    lichaamslengte = me.EmbeddedDocumentField(Lichaamslengte)


class User(me.Document):
    user_id = me.IntField()
    geboortedatum = me.DateTimeField()
    geslacht = me.StringField(choices=GESLACHTSSOORT)   #'UN', 'M', 'F', 'UNK'
    naamgegevens = me.EmbeddedDocumentField(NaamgegevensUser)
    userdata = me.EmbeddedDocumentField(UserData)
    username = me.EmailField()
    password = me.StringField()
#
#
# class Questionair(me.Document):
#     questionair_id = me.ReferenceField(User)
#     question = me.StringField()
#     answer = me.StringField()
#
#
# class Schedule(me.Document):
#     schedule_id = me.ReferenceField(User)
#     beschrijving = me.StringField()
#     datum = me.DateTimeField()
