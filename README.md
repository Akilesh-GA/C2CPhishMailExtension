# C2CPhishMailExtension

**C2CPhishMailExtension** is a Chrome browser extension designed to detect phishing emails using Natural Language Processing (NLP) techniques. This tool helps users identify whether an email is legitimate or a phishing attempt, enhancing security and awareness within web-based email platforms.

---

## 🚀 Features

- 🔍 **Phishing Detection** using NLP-based classification
- 📧 Works on popular webmail interfaces (e.g., Gmail, Outlook Web)
- 🔐 Highlights suspicious content in real-time
- 📊 Shows confidence score of phishing classification
- 🧠 Lightweight, fast, and privacy-friendly

---

## 🛠️ How It Works

1. The extension scans the content of opened emails in the browser.
2. The text is passed through a Natural Language Processing model trained to classify phishing emails.
3. Results are shown as:
   - ✅ Legitimate Email
   - ⚠️ Suspicious / Phishing Email

---

## 🧠 Technologies Used

- JavaScript (Chrome Extension API)
- HTML/CSS for popup and styling
- NLP Model (Python backend or converted JS model)
- TensorFlow.js (if model runs in-browser)
- Web scraping and content script APIs

---

## Folder Structure

C2CPhishMailExtension/
│
├── manifest.json          
├── background.js          
├── content.js             
├── popup.html             
├── popup.js               
├── style.css              
├── model/                 
└── README.md              
