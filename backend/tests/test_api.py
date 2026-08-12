def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_register_login_and_application(client):
    r = client.post("/api/auth/register", json={"name":"Shruthi","email":"test@example.com","password":"Password123"})
    assert r.status_code == 201
    token = client.post("/api/auth/login", json={"email":"test@example.com","password":"Password123"}).json()["access_token"]
    h = {"Authorization": f"Bearer {token}"}
    r = client.post("/api/applications", headers=h, json={"company":"Accenture","role":"AI/ML Engineer"})
    assert r.status_code == 201
    assert r.json()["status"] == "applied"

def test_email_classifier_flow(client):
    client.post("/api/auth/register", json={"name":"Shruthi","email":"email@example.com","password":"Password123"})
    token = client.post("/api/auth/login", json={"email":"email@example.com","password":"Password123"}).json()["access_token"]
    h = {"Authorization": f"Bearer {token}"}
    app = client.post("/api/applications", headers=h, json={"company":"DemoCo","role":"ML Engineer"}).json()
    r = client.post("/api/emails/analyze", headers=h, json={"application_id":app["id"],"sender":"hr@democo.com","subject":"Interview Invitation","body":"We would like to invite you to a technical interview."})
    assert r.status_code == 200
    assert r.json()["classification"] == "interview"
