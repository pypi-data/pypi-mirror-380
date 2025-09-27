from __future__ import annotations
from typing import Any, Optional, Literal, TypedDict, Callable
from dataclasses import dataclass
from datetime import datetime
from enum import Enum
import urllib.parse
import json
import base64
import requests


class AccountKind(str, Enum):
    STUDENT = "E"


class GradeKind(int, Enum):
    ERROR = -1
    GRADE = 0
    ABSENT = 1
    EXEMPTED = 2
    NOT_GRADED = 3
    WAITING = 4


class FileKind(str, Enum):
    CLOUD = "CLOUD"
    HOMEWORK = "FICHIER_CDT"
    ATTACHMENT = "PIECE_JOINTE"
    CANTINE_MENU = "FICHIER_MENU_RESTAURATION"
    ADMINISTRATIVE = "ADMINISTRATIF"
    OTHER = ""


class DocumentKind(str, Enum):
    GRADES = "Note"
    DOCUMENT = "Doc"
    SCHOOL_LIFE = "Viesco"
    INVOICE = "Fac"
    REGISTRATION = "Inscr"
    TEXTBOOK = "FICHIER_CDT"
    OTHER = ""


class AttendanceItemKind(str, Enum):
    PUNITION = "Punition"
    RETARD = "Retard"
    ABSENCE = "Absence"
    DISPENSE = "Dispense"


class TimetableItemKind(str, Enum):
    COURS = "COURS"
    PERMANENCE = "PERMANENCE"
    CONGE = "CONGE"
    EVENEMENT = "EVENEMENT"
    SANCTION = "SANCTION"


class TimelineItemKind(str, Enum):
    NOTE = "Note"
    VIE_SCOLAIRE = "VieScolaire"
    REUNION_PP = "ReunionPP"
    REUNION_PP_FAMILLE = "ReunionPPFamille"
    ACTUALITE = "Actualite"
    MESSAGERIE = "Messagerie"
    DOCUMENT_FAMILLE = "DocumentFamille"
    DOCUMENT = "Document"


class WorkspaceItemKind(str, Enum):
    LIBRE = "LIBRE"


class BadCredentials(Exception):
    pass


class DoubleAuthRequired(Exception):
    pass


class InvalidVersion(Exception):
    pass


class SessionTokenRequired(Exception):
    pass


class BadDoubleAuth(Exception):
    pass


@dataclass
class DoubleAuth:
    name: str
    value: str


@dataclass
class DoubleAuthChallenge:
    question: str
    answers: list[str]


@dataclass
class Session:
    username: str
    device_uuid: str
    token: Optional[str] = None
    access_token: Optional[str] = None
    double_auth: Optional[DoubleAuth] = None
    fetcher: Optional[Callable] = None


@dataclass
class Account:
    login_id: int
    id: int
    user_id: str
    username: str
    kind: AccountKind
    ogec_id: str
    main: bool
    last_connection: str
    first_name: str
    last_name: str
    email: str
    phone: str
    school_name: str
    school_uai: str
    school_logo_path: str
    school_agenda_color: str
    access_token: str
    socket_token: str
    gender: Literal["M", "F"]
    profile_picture_url: str
    modules: list[Any]
    current_school_cycle: str
    class_short: str
    class_long: str


@dataclass
class GradeValue:
    kind: GradeKind
    points: float


@dataclass
class Skill:
    id: int
    value: float
    description: str
    name: str


@dataclass
class Subject:
    id: str
    sub_subject_id: Optional[str]
    name: str


@dataclass
class Grade:
    comment: str
    exam_type: str
    period_id: str
    period_name: str
    subject: Subject
    coefficient: float
    value: GradeValue
    max_value: GradeValue
    min_value: GradeValue
    average: GradeValue
    is_optional: bool
    out_of: float
    date: datetime
    subject_file_path: str
    correction_file_path: str
    skills: list[Skill]


@dataclass
class Period:
    id: str
    name: str
    yearly: bool
    is_mock_exam: bool
    is_ended: bool
    start_date: datetime
    end_date: datetime
    council_date: Optional[datetime] = None
    council_start_hour: Optional[str] = None
    council_end_hour: Optional[str] = None
    council_classroom: Optional[str] = None


@dataclass
class SubjectOverview:
    name: str
    id: str
    child_subject_id: str
    is_child_subject: bool
    color: str
    coefficient: float
    class_average: GradeValue
    max_average: GradeValue
    min_average: GradeValue
    student_average: GradeValue
    out_of: GradeValue


@dataclass
class PeriodOverview:
    class_average: GradeValue
    overall_average: GradeValue
    subjects: list[SubjectOverview]


@dataclass
class Document:
    id: int
    name: str
    date: datetime
    kind: DocumentKind
    signature_required: bool
    signature: Optional[Any] = None


@dataclass
class Homework:
    id: int
    subject: str
    teacher: str
    exam: bool
    done: bool
    content: str
    created_date: datetime
    attachments: list[Document]


@dataclass
class ComingHomework:
    id: int
    subject: str
    is_exam: bool
    done: bool
    created_date: datetime


@dataclass
class ClassSubject:
    date: datetime
    id: int
    subject: str
    teacher: str
    content: str
    attachments: list[Document]


@dataclass
class AttendanceItem:
    id: int
    student_id: int
    student_name: str
    reason: str
    date: datetime
    date_of_event: datetime
    label: str
    teacher: str
    comment: str
    subject_name: str
    justified: bool
    justification_type: str
    online_justification: bool
    todo: str
    kind: AttendanceItemKind
    display_date: str


@dataclass
class CantineMeals:
    breakfast: bool
    lunch: bool
    diner: bool


@dataclass
class CantineReservations:
    badge: int
    diet: str
    meals: dict[str, CantineMeals]


@dataclass
class CantineBarcode:
    badge_number: int


@dataclass
class TimetableItem:
    id: int
    color: str
    start_date: datetime
    end_date: datetime
    subject_name: str
    subject_short_name: str
    room: str
    teacher: str
    kind: TimetableItemKind
    cancelled: bool
    updated: bool
    notes: str


@dataclass
class TimelineItem:
    title: str
    description: str
    content: str
    element_id: int
    element_kind: TimelineItemKind
    date: datetime


@dataclass
class HomepageTimelineItem:
    id: str
    content: str
    author_name: str
    creation_date: datetime
    start_date: datetime
    end_date: datetime
    color_name: str


@dataclass
class WorkspaceItem:
    id: str
    title: str
    description: str
    summary: str
    cloud: bool
    discussion: bool
    agenda: bool
    is_public: bool
    is_open: bool
    kind: WorkspaceItemKind
    is_member: bool
    is_admin: bool
    teacher_rooms: bool
    created_by: str
    permissions: int
    nb_members: int
    color_event_agenda: str
    created_at: Optional[str] = None


@dataclass
class ReceivedMessage:
    id: int
    type: str
    date: datetime
    read: bool
    subject: str
    can_answer: bool
    content: str
    sender: str
    files: list[dict[str, Any]]


class Request:
    def __init__(self, path: str):
        self.url = f"https://api.ecoledirecte.com/v3{path}"
        self.headers = {"User-Agent": "Android EDMOBILE v7.0.1"}
        self.method = "POST"
        self.content = None
        self.params = {"v": "7.0.1"}

    def set_token(self, token: str) -> Request:
        self.headers["X-Token"] = token
        return self

    def set_form_data(self, body: dict) -> Request:
        self.content = f"data={json.dumps(body)}"
        self.headers["Content-Type"] = "application/x-www-form-urlencoded"
        return self

    def send(self, fetcher: Optional[Callable] = None) -> Response:
        if fetcher:
            return fetcher(self)
        response = requests.post(
            self.url,
            params=self.params,
            headers=self.headers,
            data=self.content
        )
        return Response(response)

    def send_raw(self, fetcher: Optional[Callable] = None) -> requests.Response:
        if fetcher:
            return fetcher(self)
        return requests.post(
            self.url,
            params=self.params,
            headers=self.headers,
            data=self.content
        )


class Response:
    def __init__(self, response: requests.Response):
        self.token = response.headers.get("x-token")
        self.access_token = None
        self.message = None
        self.data = None

        content_type = response.headers.get("content-type", "")
        content = response.text

        valid_json = (content.startswith("[") or content.startswith("{")) and \
                     (content.endswith("]") or content.endswith("}"))

        if not content_type.startswith("application/json") and not valid_json:
            self.status = int(response.headers.get("x-code", 500))
        else:
            parsed = json.loads(content)
            self.status = parsed.get("code")
            self.data = parsed.get("data")
            self.message = parsed.get("message")
            if "token" in parsed:
                self.token = parsed["token"]


def decode_string(value: str, escape_string: bool = True) -> str:
    decoded = base64.b64decode(value).decode("utf-8")
    if escape_string:
        return urllib.parse.unquote(decoded)
    return decoded


def encode_string(value: str) -> str:
    return base64.b64encode(value.encode("utf-8")).decode("utf-8")


def decode_account_kind(kind: Any) -> AccountKind:
    kind = str(kind)
    if kind not in [e.value for e in AccountKind]:
        raise ValueError(f"Unknown AccountKind: {kind}")
    return AccountKind(kind)


def decode_account(account: dict) -> Account:
    gender = account.get("profile", {}).get("sexe")
    if not gender:
        gender = "F" if account.get("civilite") == "Mme" else "M"

    return Account(
        login_id=account["idLogin"],
        id=account["id"],
        user_id=account["uid"],
        username=account["identifiant"],
        kind=decode_account_kind(account["typeCompte"]),
        ogec_id=account["codeOgec"],
        main=account["main"],
        last_connection=account["lastConnexion"],
        first_name=account["prenom"],
        last_name=account["nom"],
        email=account["email"],
        phone=account.get("profile", {}).get("telPortable", ""),
        school_name=account["nomEtablissement"],
        school_uai=account.get("profile", {}).get("rneEtablissement", ""),
        school_logo_path=account["logoEtablissement"],
        school_agenda_color=account["couleurAgendaEtablissement"],
        access_token=account["accessToken"],
        socket_token=account["socketToken"],
        gender=gender,
        profile_picture_url=account.get("profile", {}).get("photo", ""),
        modules=account["modules"],
        current_school_cycle=account["anneeScolaireCourante"],
        class_short=account.get("profile", {}).get("classe", {}).get("code", ""),
        class_long=account.get("profile", {}).get("classe", {}).get("libelle", "")
    )


def decode_grade_value(value: str) -> GradeValue:
    if not value:
        return GradeValue(kind=GradeKind.ERROR, points=0)

    value = value.strip()
    if value == "Disp":
        return GradeValue(kind=GradeKind.EXEMPTED, points=0)
    elif value == "Abs":
        return GradeValue(kind=GradeKind.ABSENT, points=0)
    elif value == "NE":
        return GradeValue(kind=GradeKind.NOT_GRADED, points=0)
    elif value == "EA":
        return GradeValue(kind=GradeKind.WAITING, points=0)
    else:
        try:
            return GradeValue(kind=GradeKind.GRADE, points=float(value.replace(",", ".")))
        except:
            return GradeValue(kind=GradeKind.ERROR, points=0)


def decode_skill(item: dict) -> Skill:
    return Skill(
        id=item["idCompetence"],
        value=float(item["valeur"]),
        description=item["descriptif"],
        name=item["libelleCompetence"]
    )


def decode_grade(item: dict) -> Grade:
    return Grade(
        comment=item["devoir"],
        exam_type=item["typeDevoir"],
        period_id=item["codePeriode"],
        period_name="",
        subject=Subject(
            id=item["codeMatiere"],
            sub_subject_id=item.get("codeSousMatiere"),
            name=item["libelleMatiere"]
        ),
        coefficient=float(item["coef"]),
        value=decode_grade_value(item["valeur"]),
        max_value=decode_grade_value(item["maxClasse"]),
        min_value=decode_grade_value(item["minClasse"]),
        average=decode_grade_value(item["moyenneClasse"]),
        is_optional=item["valeurisee"],
        out_of=float(item["noteSur"].replace(",", ".")),
        date=datetime.strptime(item["date"], "%Y-%m-%d"),
        subject_file_path=item.get("uncSujet", ""),
        correction_file_path=item.get("uncCorrige", ""),
        skills=[decode_skill(s) for s in item.get("elementsProgramme", [])]
    )


def decode_period(item: dict) -> Period:
    return Period(
        id=item["idPeriode"],
        name=item["periode"],
        yearly=item["annuel"],
        is_mock_exam=item["examenBlanc"],
        is_ended=item["cloture"],
        start_date=datetime.strptime(item["dateDebut"], "%Y-%m-%d"),
        end_date=datetime.strptime(item["dateFin"], "%Y-%m-%d"),
        council_date=datetime.strptime(item["dateConseil"], "%Y-%m-%d") if item.get("dateConseil") else None,
        council_start_hour=item.get("heureConseil"),
        council_end_hour=item.get("heureFinConseil"),
        council_classroom=item.get("salleConseil")
    )


def build_overview(data: dict) -> dict[str, PeriodOverview]:
    overview = {}
    out_of = data.get("parametrage", {}).get("moyenneSur", 20)
    show_student_average = data.get("parametrage", {}).get("moyenneGenerale", True)
    show_yearly_period = data.get("parametrage", {}).get("notePeriodeAnnuelle", True)

    for period in data.get("periodes", []):
        if show_yearly_period is False and period.get("yearly"):
            continue

        subjects = period.get("ensembleMatieres", {}).get("disciplines", [])
        
        class_avg = decode_grade_value(period.get("ensembleMatieres", {}).get("moyenneClasse", ""))
        
        if show_student_average:
            overall_avg = decode_grade_value(period.get("ensembleMatieres", {}).get("moyenneGenerale", ""))
        else:
            count = 0
            total = 0
            for subject in subjects:
                if subject.get("moyenne", "") != "":
                    grade = decode_grade_value(subject["moyenne"].replace(",", ".")).points
                    coef = subject.get("coef", 1) if subject.get("coef", 1) != 0 else 1
                    count += coef
                    total += grade * coef
            overall_avg = decode_grade_value(str(total / count if count > 0 else 0))

        subject_overviews = []
        for subject in subjects:
            subject_overviews.append(SubjectOverview(
                name=subject["discipline"],
                id=subject["codeMatiere"],
                child_subject_id=subject.get("codeSousMatiere", ""),
                is_child_subject=subject.get("sousMatiere", False),
                color="",
                coefficient=float(subject.get("coef", 1)),
                class_average=decode_grade_value(subject.get("moyenneClasse", "").replace(",", ".")),
                max_average=decode_grade_value(subject.get("moyenneMax", "").replace(",", ".")),
                min_average=decode_grade_value(subject.get("moyenneMin", "").replace(",", ".")),
                student_average=decode_grade_value(subject.get("moyenne", "").replace(",", ".")),
                out_of=decode_grade_value(str(out_of))
            ))

        overview[period["idPeriode"]] = PeriodOverview(
            class_average=class_avg,
            overall_average=overall_avg,
            subjects=subject_overviews
        )

    return overview


def decode_document(item: dict) -> Document:
    return Document(
        id=item["id"],
        name=item["libelle"],
        date=datetime.strptime(item["date"], "%Y-%m-%d"),
        kind=DocumentKind(item.get("type", "")),
        signature_required=item.get("signatureDemandee", False),
        signature=item.get("signature")
    )


def decode_homework(item: dict) -> Homework:
    return Homework(
        id=item["id"],
        subject=item["matiere"],
        teacher=item["nomProf"],
        exam=item["interrogation"],
        done=item["aFaire"]["effectue"],
        content=decode_string(item["aFaire"]["contenu"]),
        created_date=datetime.strptime(item["aFaire"]["donneLe"], "%Y-%m-%d"),
        attachments=[decode_document(d) for d in item["aFaire"].get("documents", [])]
    )


def decode_coming_homework(item: dict) -> ComingHomework:
    return ComingHomework(
        id=item["idDevoir"],
        subject=item["matiere"],
        is_exam=item["interrogation"],
        done=item["effectue"],
        created_date=datetime.strptime(item["donneLe"], "%Y-%m-%d")
    )


def decode_class_subject(item: dict, date: datetime) -> ClassSubject:
    content = item.get("contenuDeSeance", {}).get("contenu", "")
    return ClassSubject(
        date=date,
        id=item["id"],
        subject=item["matiere"],
        teacher=item["nomProf"],
        content=decode_string(content) if content else "",
        attachments=[decode_document(d) for d in item.get("contenuDeSeance", {}).get("documents", [])]
    )


def decode_attendance_item(item: dict) -> AttendanceItem:
    display_date = item.get("displayDate", "")
    if not display_date:
        display_date = item.get("dateDeroulement", "").lower().replace("<br>", " ").replace("déroulement prévu ", "")

    return AttendanceItem(
        id=item["id"],
        student_id=item["idEleve"],
        student_name=item["nomEleve"],
        reason=item["motif"],
        date=datetime.strptime(item["date"], "%Y-%m-%d"),
        date_of_event=datetime.strptime(item["dateDeroulement"], "%Y-%m-%d"),
        label=item["libelle"],
        teacher=item["par"],
        comment=item["commentaire"],
        subject_name=item["matiere"],
        justified=item["justifie"],
        justification_type=item["typeJustification"],
        online_justification=item["justifieEd"],
        todo=item["aFaire"],
        kind=AttendanceItemKind(item["typeElement"]),
        display_date=display_date
    )


def decode_cantine_reservations(item: dict) -> CantineReservations:
    params = item.get("params", {})
    meals = {
        "monday": CantineMeals(False, params.get("repasmidi_1") == "1", params.get("repassoir_1") == "1"),
        "tuesday": CantineMeals(False, params.get("repasmidi_2") == "1", params.get("repassoir_2") == "1"),
        "wednesday": CantineMeals(False, params.get("repasmidi_3") == "1", params.get("repassoir_3") == "1"),
        "thursday": CantineMeals(False, params.get("repasmidi_4") == "1", params.get("repassoir_4") == "1"),
        "friday": CantineMeals(False, params.get("repasmidi_5") == "1", params.get("repassoir_5") == "1"),
        "saturday": CantineMeals(False, params.get("repasmidi_6") == "1", params.get("repassoir_6") == "1"),
        "sunday": CantineMeals(False, params.get("repasmidi_7") == "1", params.get("repassoir_7") == "1"),
    }
    return CantineReservations(
        badge=item.get("badge", 0),
        diet=params.get("regime", ""),
        meals=meals
    )


def decode_cantine_barcode(item: dict) -> CantineBarcode:
    return CantineBarcode(badge_number=item.get("params", {}).get("numeroBadge", 0))


def decode_timetable_item(item: dict) -> TimetableItem:
    return TimetableItem(
        id=item["id"],
        color=item["color"],
        start_date=datetime.fromisoformat(item["start_date"]),
        end_date=datetime.fromisoformat(item["end_date"]),
        subject_name=item["matiere"],
        subject_short_name=item["codeMatiere"],
        room=item["salle"],
        teacher=item["prof"],
        kind=TimetableItemKind(item["typeCours"]),
        cancelled=item["isAnnule"],
        updated=item["isModifie"],
        notes=item["text"]
    )


def decode_timeline_item(item: dict) -> TimelineItem:
    return TimelineItem(
        title=item["titre"],
        description=item["soustitre"],
        content=item["contenu"],
        element_id=item["idElement"],
        element_kind=TimelineItemKind(item["typeElement"]),
        date=datetime.fromisoformat(item["date"])
    )


def decode_french_date(date_str: str) -> datetime:
    day, month, year = date_str.split("/")
    return datetime(int(year), int(month), int(day))


def decode_homepage_timeline_item(item: dict) -> HomepageTimelineItem:
    return HomepageTimelineItem(
        id=item["id"],
        content=decode_string(item["contenu"]),
        author_name=item["auteur"]["nom"],
        creation_date=decode_french_date(item["dateCreation"]),
        start_date=decode_french_date(item["dateDebut"]),
        end_date=decode_french_date(item["dateFin"]),
        color_name=item["type"]
    )


def decode_workspace_item(item: dict) -> WorkspaceItem:
    return WorkspaceItem(
        id=item["id"],
        title=item["titre"],
        description=item["description"],
        summary=decode_string(item["resume"]),
        cloud=item["cloud"],
        discussion=item["discussion"],
        agenda=item["agenda"],
        is_public=item["public"],
        is_open=item["ouvert"],
        kind=WorkspaceItemKind(item["type"]),
        is_member=item["estMembre"],
        is_admin=item["estAdmin"],
        teacher_rooms=item["salleDesProfs"],
        created_by=item["creePar"],
        permissions=item["droitUtilisateur"],
        nb_members=item["nbMembres"],
        color_event_agenda=item["couleurEvenementAgenda"],
        created_at=item.get("creeLe")
    )


def decode_message_list(message: dict) -> ReceivedMessage:
    sender_data = message.get("from", {})
    return ReceivedMessage(
        id=message["id"],
        type=message["mtype"],
        date=datetime.fromisoformat(message["date"]),
        read=message["read"],
        subject=message["subject"],
        can_answer=message["canAnswer"],
        content=message.get("content", ""),
        sender=f"{sender_data.get('prenom', '')} {sender_data.get('nom', '')}",
        files=[{
            "id": f["id"],
            "name": f["libelle"],
            "type": FileKind(f["type"])
        } for f in message.get("files", [])]
    )


def encode_double_auth(double_auth: Optional[DoubleAuth]) -> Optional[dict]:
    if not double_auth:
        return None
    return {"cn": double_auth.name, "cv": double_auth.value}


def decode_double_auth_challenge(challenge: dict) -> DoubleAuthChallenge:
    return DoubleAuthChallenge(
        question=decode_string(challenge["question"]),
        answers=[decode_string(a) for a in challenge["propositions"]]
    )


def decode_double_auth(double_auth: Any) -> DoubleAuth:
    if double_auth is None:
        raise BadDoubleAuth()
    return DoubleAuth(name=double_auth["cn"], value=double_auth["cv"])


def init_login(body: dict, token: Optional[str] = None) -> Request:
    request_gtk = Request("/login.awp?gtk=1")
    response_gtk = request_gtk.send_raw()
    
    cookies = []
    gtk = None
    
    for cookie in response_gtk.cookies:
        cookies.append(f"{cookie.name}={cookie.value}")
        if cookie.name == "GTK":
            gtk = cookie.value
    
    if not gtk:
        raise Exception("GTK cookie not found")
    
    request = Request("/login.awp")
    request.set_form_data(body)
    request.headers["X-GTK"] = gtk
    request.headers["Cookie"] = "; ".join(cookies)
    
    if token:
        request.set_token(token)
    
    return request


def login(session: Session, password: str) -> list[Account]:
    encoded_double_auth = encode_double_auth(session.double_auth)
    
    body = {
        "identifiant": session.username,
        "uuid": session.device_uuid,
        "isReLogin": False,
        "sesouvenirdemoi": True,
        "motdepasse": urllib.parse.quote(password)
    }
    
    if encoded_double_auth:
        body.update(encoded_double_auth)
        body["fa"] = [encoded_double_auth]
    
    request = init_login(body, session.token)
    response = request.send(session.fetcher)
    
    session.token = response.token
    
    if response.status == 505:
        raise BadCredentials()
    elif response.status == 517:
        raise InvalidVersion()
    elif response.status == 250:
        raise DoubleAuthRequired()
    
    return [decode_account(acc) for acc in response.data.get("accounts", [])]


def refresh(session: Session, account_kind: AccountKind) -> list[Account]:
    if not session.token:
        raise SessionTokenRequired()
    
    body = {
        "fa": [encode_double_auth(session.double_auth)],
        "identifiant": session.username,
        "uuid": session.device_uuid,
        "isReLogin": True,
        "motdepasse": "???",
        "typeCompte": account_kind.value,
        "accesstoken": session.access_token
    }
    
    request = init_login(body, session.token)
    response = request.send(session.fetcher)
    
    session.token = response.token
    
    if response.status == 505:
        raise BadCredentials()
    elif response.status == 517:
        raise InvalidVersion()
    elif response.status == 250:
        raise DoubleAuthRequired()
    
    return [decode_account(acc) for acc in response.data.get("accounts", [])]


def set_access_token(session: Session, account: Account):
    session.access_token = account.access_token


def init_double_auth(session: Session) -> DoubleAuthChallenge:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request("/connexion/doubleauth.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    
    if not response.token:
        raise BadCredentials()
    
    session.token = response.token
    return decode_double_auth_challenge(response.data)


def check_double_auth(session: Session, answer: str) -> bool:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request("/connexion/doubleauth.awp?verbe=post")
    request.set_token(session.token).set_form_data({
        "choix": encode_string(answer)
    })
    
    response = request.send(session.fetcher)
    session.token = response.token
    session.double_auth = decode_double_auth(response.data)
    
    return True


def student_grades(session: Session, account: Account, year: str = "") -> dict:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/eleves/{account.id}/notes.awp?verbe=get")
    request.set_token(session.token).set_form_data({"anneeScolaire": year})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    grades = [decode_grade(g) for g in response.data.get("notes", [])]
    periods_data = response.data.get("periodes", [])
    show_yearly = response.data.get("parametrage", {}).get("notePeriodeAnnuelle", True)
    
    periods = [decode_period(p) for p in periods_data if not (show_yearly is False and p.get("yearly"))]
    overview = build_overview(response.data)
    
    return {"grades": grades, "periods": periods, "overview": overview}


def student_homeworks(session: Session, account: Account, date: str) -> dict:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/Eleves/{account.id}/cahierdetexte/{date}.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    matieres = response.data.get("matieres", [])
    homeworks = [decode_homework(h) for h in matieres if h.get("aFaire")]
    
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    subjects = [decode_class_subject(item, date_obj) for item in matieres]
    subjects = [s for s in subjects if s.attachments or s.content]
    
    return {"homeworks": homeworks, "subjects": subjects}


def student_coming_homeworks(session: Session, account: Account) -> list[dict]:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/Eleves/{account.id}/cahierdetexte.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    result = []
    for date_str, homeworks in response.data.items():
        result.append({
            "date": datetime.strptime(date_str, "%Y-%m-%d"),
            "homeworks": [decode_coming_homework(h) for h in homeworks]
        })
    
    return result


def set_homework_state(session: Session, account: Account, homework_id: int, done: bool):
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/Eleves/{account.id}/cahierdetexte.awp?verbe=put")
    request.set_token(session.token).set_form_data({
        "idDevoirsEffectues": [homework_id if done else None],
        "idDevoirsNonEffectues": [None if done else homework_id]
    })
    
    request.send(session.fetcher)


def student_attendance(session: Session, account: Account) -> dict:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/eleves/{account.id}/viescolaire.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    return {
        "punishments": [decode_attendance_item(p) for p in response.data.get("sanctionsEncouragements", [])],
        "absences": [decode_attendance_item(a) for a in response.data.get("absencesRetards", [])],
        "exemptions": [decode_attendance_item(e) for e in response.data.get("dispenses", [])]
    }


def student_cantine(account: Account) -> dict:
    reservations_module = next((m for m in account.modules if m.get("code") == "RESERVATIONS"), None)
    barcode_module = next((m for m in account.modules if m.get("code") == "CANTINE_BARCODE"), None)
    
    result = {}
    
    if reservations_module and reservations_module.get("enable"):
        result["reservation"] = decode_cantine_reservations(reservations_module)
    
    if barcode_module and barcode_module.get("enable"):
        result["barcode"] = decode_cantine_barcode(barcode_module)
    
    return result


def student_documents(session: Session, archive: str = "") -> list[Document]:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/elevesDocuments.awp?verbe=get&archive={archive}")
    request.set_token(session.token).set_form_data({"forceDownload": 0})
    
    response = request.send(session.fetcher)
    
    all_documents = []
    for key in ["factures", "notes", "viescolaire", "administratifs", "inscriptions"]:
        all_documents.extend(response.data.get(key, []))
    
    return [decode_document(d) for d in all_documents]


def build_file_download_url(file_type: FileKind, file_id: int, year: str = "") -> str:
    endpoint = f"/telechargement.awp?verbe=get&fichierId={file_id}"
    
    if file_type == FileKind.ADMINISTRATIVE:
        if year:
            return f"{endpoint}&archive=true&anneeArchive={year}"
        return endpoint
    elif file_type == FileKind.ATTACHMENT:
        if year:
            return f"{endpoint}&anneeMessages={year}"
        return endpoint
    else:
        return f"{endpoint}&leTypeDeFichier={file_type.value}"


def get_file(session: Session, file_type: FileKind, file_id: int, year: str = "") -> requests.Response:
    if not session.token:
        raise SessionTokenRequired()
    
    url = build_file_download_url(file_type, file_id, year)
    request = Request(url)
    request.set_token(session.token).set_form_data({"forceDownload": 0})
    
    return request.send_raw(session.fetcher)


def student_timetable(session: Session, account: Account, start_date: datetime, end_date: Optional[datetime] = None) -> list[TimetableItem]:
    if not session.token:
        raise SessionTokenRequired()
    
    if end_date is None:
        end_date = start_date
    
    request = Request(f"/E/{account.id}/emploidutemps.awp?verbe=get")
    request.set_token(session.token).set_form_data({
        "dateDebut": start_date.strftime("%Y-%m-%d"),
        "dateFin": end_date.strftime("%Y-%m-%d"),
        "avecTrous": False
    })
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    items = [decode_timetable_item(item) for item in response.data]
    items.sort(key=lambda x: x.start_date)
    
    return items


def student_timeline(session: Session, account: Account) -> list[TimelineItem]:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/eleves/{account.id}/timeline.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    return [decode_timeline_item(item) for item in response.data]


def student_homepage_timeline(session: Session, account: Account) -> list[HomepageTimelineItem]:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/E/{account.id}/timelineAccueilCommun.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    return [decode_homepage_timeline_item(item) for item in response.data.get("postits", [])]


def student_workspace(session: Session, account: Account) -> list[WorkspaceItem]:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/E/{account.id}/espacestravail.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    return [decode_workspace_item(item) for item in response.data or []]


def student_visios(session: Session, account: Account) -> list:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/eleves/{account.id}/visios.awp?verbe=get")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    return response.data


def account_edforms(session: Session, account: Account) -> list:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request("/edforms.awp?verbe=list")
    request.set_token(session.token).set_form_data({
        "idEntity": account.id,
        "typeEntity": account.kind.value
    })
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    return response.data


def student_received_messages(session: Session, account: Account) -> dict:
    if not session.token:
        raise SessionTokenRequired()
    
    current_year = datetime.now().year
    request = Request(f"/eleves/{account.id}/messages.awp?verbe=get&getAll=1")
    request.set_token(session.token).set_form_data({
        "anneeMessages": f"{current_year}-{current_year + 1}"
    })
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    parametrage = response.data.get("parametrage", {})
    can_reply = (
        parametrage.get("destAdmin", False) or
        parametrage.get("destEleve", False) or
        parametrage.get("destEspTravail", False) or
        parametrage.get("destFamille", False) or
        parametrage.get("destProf", False)
    )
    
    messages = [decode_message_list(m) for m in response.data.get("messages", {}).get("received", [])]
    messages.sort(key=lambda x: x.date, reverse=True)
    
    return {"chats": messages, "can_reply": can_reply}


def read_message(session: Session, account: Account, message_id: int) -> ReceivedMessage:
    if not session.token:
        raise SessionTokenRequired()
    
    request = Request(f"/eleves/{account.id}/messages/{message_id}.awp?verbe=get&mode=destinataire")
    request.set_token(session.token).set_form_data({})
    
    response = request.send(session.fetcher)
    session.token = response.token
    
    data = response.data
    sender_data = data.get("from", {})
    
    return ReceivedMessage(
        id=data["id"],
        type=data["mtype"],
        date=datetime.fromisoformat(data["date"]),
        read=data["read"],
        subject=data["subject"],
        can_answer=data["canAnswer"],
        content=decode_string(data["content"]),
        sender=f"{sender_data.get('prenom', '')} {sender_data.get('nom', '')}",
        files=[{
            "id": f["id"],
            "name": f["libelle"],
            "type": FileKind(f["type"])
        } for f in data.get("files", [])]
    )