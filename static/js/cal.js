// script.js
document.addEventListener('DOMContentLoaded', () => {
    const fetchButton = document.getElementById('fetch-co2-data');
    const calculateButton = document.getElementById('calculate');
    const co2Input = document.getElementById('co2');
    const resultSpan = document.getElementById('result');
  
    // CO₂ 데이터 불러오기 버튼 클릭 이벤트
    fetchButton.addEventListener('click', async () => {
      try {
        // 센서 데이터를 제공하는 API 엔드포인트
        const apiUrl = 'http://sensor-api-endpoint.com/co2-data';
  
        // API 호출
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error(`API 요청 실패: ${response.statusText}`);
        }
  
        // JSON 데이터 추출
        const data = await response.json();
  
        // CO₂ 데이터가 제대로 왔는지 확인 후 값 설정
        if (data && data.co2) {
          co2Input.value = data.co2; // 센서 데이터를 입력 필드에 표시
        } else {
          alert('센서 데이터가 올바르지 않습니다!');
        }
      } catch (error) {
        console.error('CO₂ 데이터를 불러오는 중 오류 발생:', error);
        alert('센서 데이터를 불러오는 중 문제가 발생했습니다. 다시 시도하세요.');
      }
    });
  
    // 계산하기 버튼 클릭 이벤트
    calculateButton.addEventListener('click', () => {
      const co2Value = parseFloat(co2Input.value);
  
      if (isNaN(co2Value) || co2Value <= 0) {
        alert('유효한 CO₂ 값을 입력하세요!');
        return;
      }
  
      // 간단한 계산 로직: 월별 배출량을 연간 배출량으로 변환
      const annualEmission = co2Value * 12;
  
      // 결과 표시
      resultSpan.textContent = annualEmission.toLocaleString(); // 숫자 포맷
    });
  });
  
