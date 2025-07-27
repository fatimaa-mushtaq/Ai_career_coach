def render_resume_html(name, email, cnic, address, degree, skills, interests, goal, image_url):
    return f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <style>
    body {{
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }}
    .container {{
      width: 800px;
      margin: 40px auto;
      background: #fff;
      border-radius: 10px;
      overflow: hidden;
      box-shadow: 0 4px 10px rgba(0,0,0,0.2);
    }}
    .top {{
      display: flex;
      background: #0f172a;
      color: white;
      padding: 20px;
      align-items: center;
    }}
    .photo {{
      flex: 1;
    }}
    .photo img {{
      width: 120px;
      height: 120px;
      border-radius: 10px;
      object-fit: cover;
    }}
    .info {{
      flex: 3;
      padding-left: 20px;
    }}
    .section {{
      padding: 25px 30px;
      border-bottom: 1px solid #ccc;
    }}
    h2 {{
      margin-bottom: 10px;
      color: #1f2937;
      border-left: 4px solid #3b82f6;
      padding-left: 10px;
    }}
    p {{
      margin: 5px 0;
    }}
    ul {{
      padding-left: 20px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="top">
      <div class="photo">
        <img src="{image_url}" alt="Profile Photo" />
      </div>
      <div class="info">
        <h1>{name}</h1>
        <p><strong>Email:</strong> {email}</p>
        <p><strong>CNIC:</strong> {cnic}</p>
        <p><strong>Address:</strong> {address}</p>
      </div>
    </div>
    <div class="section">
      <h2>🎓 Education</h2>
      <p>{degree}</p>
    </div>
    <div class="section">
      <h2>🧠 Skills</h2>
      <p>{skills}</p>
    </div>
    <div class="section">
      <h2>💡 Interests</h2>
      <p>{interests}</p>
    </div>
    <div class="section">
      <h2>🎯 Career Goal</h2>
      <p>{goal}</p>
    </div>
  </div>
</body>
</html>
"""