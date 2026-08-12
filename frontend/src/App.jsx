import React, { useEffect, useState } from "react";

const API = "http://localhost:8000/api";

function App() {
  const [token, setToken] = useState(localStorage.getItem("clearhire_token"));
  const [applications, setApplications] = useState([]);
  const [form, setForm] = useState({ company: "", role: "" });
  const [emailForm, setEmailForm] = useState({
    application_id: "",
    sender: "",
    subject: "",
    body: "",
  });
  const [analysis, setAnalysis] = useState(null);
  const [message, setMessage] = useState("");

  async function loadApplications(currentToken = token) {
    if (!currentToken) return;

    const response = await fetch(`${API}/applications`, {
      headers: { Authorization: `Bearer ${currentToken}` },
    });

    if (response.ok) {
      const data = await response.json();
      setApplications(data);

      if (!emailForm.application_id && data.length > 0) {
        setEmailForm((current) => ({
          ...current,
          application_id: String(data[0].id),
        }));
      }
    }
  }

  async function demoLogin() {
    const email = "demo@clearhire.com";
    const password = "DemoPassword123";

    await fetch(`${API}/auth/register`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        name: "Demo Candidate",
        email,
        password,
      }),
    });

    const response = await fetch(`${API}/auth/login`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email, password }),
    });

    const data = await response.json();

    if (response.ok) {
      localStorage.setItem("clearhire_token", data.access_token);
      setToken(data.access_token);
      setMessage("Logged in as demo candidate.");
    } else {
      setMessage(data.detail || "Could not log in.");
    }
  }

  async function createApplication(event) {
    event.preventDefault();

    const response = await fetch(`${API}/applications`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify(form),
    });

    if (response.ok) {
      const created = await response.json();

      setForm({ company: "", role: "" });
      setEmailForm((current) => ({
        ...current,
        application_id: String(created.id),
      }));
      setMessage("Application added.");
      await loadApplications();
    } else {
      const data = await response.json().catch(() => ({}));
      setMessage(data.detail || "Could not add application.");
    }
  }

  async function analyzeEmail(event) {
    event.preventDefault();
    setAnalysis(null);
    setMessage("");

    const response = await fetch(`${API}/emails/analyze`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${token}`,
      },
      body: JSON.stringify({
        application_id: Number(emailForm.application_id),
        sender: emailForm.sender,
        subject: emailForm.subject,
        body: emailForm.body,
      }),
    });

    const data = await response.json();

    if (response.ok) {
      setAnalysis(data);
      setMessage("Recruiter email analyzed successfully.");
      await loadApplications();
    } else {
      setMessage(data.detail || "Could not analyze the email.");
    }
  }

  function logout() {
    localStorage.removeItem("clearhire_token");
    setToken(null);
  }

  useEffect(() => {
    loadApplications();
  }, [token]);

  if (!token) {
    return (
      <main className="landing">
        <div className="hero">
          <p className="eyebrow">CLEARHIRE AI</p>
          <h1>Know what happened.<br />Stop guessing.</h1>
          <p>
            Track job applications, detect recruiter communication and understand
            your verified next step in one place.
          </p>
          <button onClick={demoLogin}>Try demo</button>
        </div>
      </main>
    );
  }

  return (
    <main className="dashboard">
      <header>
        <div>
          <p className="eyebrow">CLEARHIRE AI</p>
          <h1>Application dashboard</h1>
        </div>
        <button className="secondary" onClick={logout}>Log out</button>
      </header>

      {message && <div className="notice">{message}</div>}

      <section className="panel">
        <h2>Add an application</h2>

        <form onSubmit={createApplication} className="application-form">
          <input
            placeholder="Company"
            value={form.company}
            onChange={(e) => setForm({ ...form, company: e.target.value })}
            required
          />
          <input
            placeholder="Role"
            value={form.role}
            onChange={(e) => setForm({ ...form, role: e.target.value })}
            required
          />
          <button type="submit">Add</button>
        </form>
      </section>

      <section className="panel email-panel">
        <div className="section-heading">
          <div>
            <p className="eyebrow">NLP ANALYSIS</p>
            <h2>Analyze recruiter email</h2>
          </div>
          <span className="ai-badge">AI</span>
        </div>

        <p className="section-description">
          Paste a recruiter message and ClearHire will classify it and update the
          selected application's status and timeline.
        </p>

        {applications.length === 0 ? (
          <div className="empty-state">
            Add an application first, then analyze a recruiter email.
          </div>
        ) : (
          <form onSubmit={analyzeEmail} className="email-form">
            <label>
              Application
              <select
                value={emailForm.application_id}
                onChange={(e) =>
                  setEmailForm({ ...emailForm, application_id: e.target.value })
                }
                required
              >
                <option value="">Select an application</option>
                {applications.map((app) => (
                  <option key={app.id} value={app.id}>
                    {app.company} — {app.role}
                  </option>
                ))}
              </select>
            </label>

            <label>
              Recruiter email
              <input
                type="email"
                placeholder="recruiter@company.com"
                value={emailForm.sender}
                onChange={(e) =>
                  setEmailForm({ ...emailForm, sender: e.target.value })
                }
                required
              />
            </label>

            <label>
              Subject
              <input
                placeholder="Interview Invitation"
                value={emailForm.subject}
                onChange={(e) =>
                  setEmailForm({ ...emailForm, subject: e.target.value })
                }
                required
              />
            </label>

            <label>
              Email body
              <textarea
                rows="6"
                placeholder="We would like to invite you to a technical interview..."
                value={emailForm.body}
                onChange={(e) =>
                  setEmailForm({ ...emailForm, body: e.target.value })
                }
                required
              />
            </label>

            <button type="submit">Analyze Email</button>
          </form>
        )}

        {analysis && (
          <div className="analysis-result">
            <div className="result-header">
              <div>
                <p className="eyebrow">ANALYSIS RESULT</p>
                <h3>Recruiter communication detected</h3>
              </div>
              <span className="classification">
                {analysis.classification}
              </span>
            </div>

            <div className="result-grid">
              <div>
                <span>Classification</span>
                <strong>{analysis.classification}</strong>
              </div>
              <div>
                <span>Confidence</span>
                <strong>{Math.round(analysis.confidence * 100)}%</strong>
              </div>
              <div>
                <span>Application status</span>
                <strong>{analysis.application_status}</strong>
              </div>
            </div>

            <div className="explanation-box">
              <strong>Explanation</strong>
              <p>{analysis.explanation}</p>
            </div>
          </div>
        )}
      </section>

      <section>
        <h2>Your applications</h2>

        <div className="cards">
          {applications.length === 0 ? (
            <div className="empty-state">
              No applications yet. Add your first application above.
            </div>
          ) : (
            applications.map((app) => (
              <article className="card" key={app.id}>
                <div className="card-top">
                  <div>
                    <h3>{app.company}</h3>
                    <p>{app.role}</p>
                  </div>
                  <span className="status">{app.status}</span>
                </div>

                <p className="explanation">
                  {app.latest_explanation ||
                    "No update has been detected yet."}
                </p>

                <div className="timeline">
                  {app.events?.map((event) => (
                    <div key={event.id}>
                      <strong>{event.event_type}</strong>
                      <span>{event.description}</span>
                    </div>
                  ))}
                </div>
              </article>
            ))
          )}
        </div>
      </section>
    </main>
  );
}

export default App;
