# LA Connect — Rider App Prototype

A clickable 9-screen mobile app prototype for **LA Connect**, the concept rider app for the
405 Rail + Bus Feeder Network: onboarding, home, trip planner, live trip, rewards, reward
detail, wallet, community, and profile — with light/dark mode and full screen-to-screen
navigation, hosted as a live Streamlit page.

**Live demo:** _(add your Streamlit Community Cloud URL here after deploying)_

## What's in this repo

| File | Purpose |
|---|---|
| `app.py` | Streamlit wrapper that embeds the prototype for public hosting |
| `la_connect_prototype.html` | The self-contained 9-screen prototype (HTML/CSS/JS in one file, no build step) |
| `requirements.txt` | Python dependencies for the Streamlit app |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Streamlit will print a local URL (usually `http://localhost:8501`) — open it in your browser.

## Deploy to Streamlit Community Cloud (free)

1. Push this project to a GitHub repo.
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in with GitHub.
3. "Create app" → "Deploy a public app from GitHub" → select the repo, branch `main`,
   main file path `app.py`.
4. Deploy — takes 1-3 minutes. Copy the resulting `https://*.streamlit.app` URL into the
   **Live demo** line above.
