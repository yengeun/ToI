# FE 수정사항
- 파일 이름 : signinup → accounts로 변경
- 경로 변경
  - main.html : ```line16) <li><a href="../../../main/templates/cal.html"><span>탄소값 계산</span></a></li>``` → ```<li><a href="{% url 'calculator:calculate' %}"><span>탄소값 계산</span></a></li> ```
  - cal.html : ```line10) <a href="../../../main/templates/main.html" class="home-button"> 홈으로 </a>``` → ```<a href="{% url 'main:dashboard' %}" class="home-button">홈으로</a> ```
  - login.html : ```line16) <form class="login-form" action="../../../main/templates/main.html">``` → ```<form class="login-form" action="{% url 'main:dashboard' %}">```
