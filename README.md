# webexbot
# 🚀 Space Bot API Investigation Sheet

**Total Marks: 40**  
**Part 1: Collect Required API Documentation**

This investigation sheet helps you gather key technical information from the three APIs required for the Space Bot project: **Webex Messaging API**, **ISS Current Location API**, and a **Geocoding API** (LocationIQ or Mapbox), plus the Python time module.

---

## ✅ Section 1: Webex Messaging API (10 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `_______________________________` |
| Authentication Method | `_______________________________` |
| Endpoint to list rooms | `_______________________________` |
| Endpoint to get messages | `_______________________________` |
| Endpoint to send message | `_______________________________` |
| Required headers | `_______________________________` |
| Sample full GET or POST request | `_______________________________` |

---

## 🛰️ Section 2: ISS Current Location API (5 marks)

| Criteria | Details |
|---------|---------|
| API Base URL | `_______________________________` |
| Endpoint for current ISS location | `_______________________________` |
| Sample response format (example JSON) |  
```
{
  "timestamp": 1234567890,
  "iss_position": {
    "latitude": "00.0000",
    "longitude": "00.0000"
  },
  "message": "success"
}
```
|

---

## 🗺️ Section 3: Geocoding API (LocationIQ or Mapbox) (15 marks)

| Criteria | Details |
|---------|---------|
| Provider used (circle one) | **LocationIQ / Mapbox** |
| API Base URL | `_______________________________` |
| Endpoint for reverse geocoding | `_______________________________` |
| Authentication method | `_______________________________` |
| Required query parameters | `_______________________________` |
| Sample request with latitude/longitude | `_______________________________` |
| Sample JSON response (formatted example) |  
```
{
  "address": {
    "road": "Main St",
    "city": "Anytown",
    "state": "CA",
    "country": "USA"
  }
}
```
|

---

## ⏰ Section 4: Epoch to Human Time Conversion (Python time module) (5 marks)

| Criteria | Details |
|---------|---------|
| Library used | `_______________________________` |
| Function used to convert epoch | `_______________________________` |
| Sample code to convert timestamp |  
```python
import time  
print(time.ctime(1660000000))  
```
|
| Output (human-readable time) | `_______________________________` |

---

## 🔍 Notes

- Use official documentation for accuracy (e.g. developer.webex.com, locationiq.com, open-notify.org).
- Be prepared to explain your findings to your instructor or demo how you retrieved them using tools like Postman, Curl, or Python scripts.

---

### ✅ Total: /40
