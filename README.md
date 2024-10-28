## 버스 모니터링 시스템
> 라즈베리 파이 및 각종 센서를 활용한 IoT 프로젝트  
> 프로젝트 기간 2021.11.14 ~ 2021.11.30
> 개발 인원 : 1명

### Description
---
버스모니터링 시스템은 초음파센서, 온도 센서를 기반으로 버스 내부의 승객의 탑승인원 데이터를 추출하고
FLASK 및 MQTT 통신을 활용해 추출한 데이터를 대시보드로 시각화 하는 IoT 기반 서비스입니다.  
초음파 센서 두개를 이용하여 승객의 승하차를 판단하고 온도센서를 통해 자동으로 에어컨을 가동시킵니다.(LED로 가정)  
시간에 따른 탑승 승객의 수를 파악하게 하여 승객에게 버스 혼잡도를 제공하고, 버스 회사에게 시간에 따른 승객 이용수 데이터를 제공할 수 있습니다.  
또한, picamera 와 openCV를 활용해 버스 내부 CCTV를 확인할 수 있습니다.

### 기술 스택
---
<table>
    <tr>
        <td style="text-align: center"> OS </td>
        <td>   
            <img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black" alt = "Linux"> 
        </td>
    </tr>
    <tr>
         <td style="text-align: center"> Tool </td> 
         <td>  
             <img src="https://img.shields.io/badge/vim-339AF0?style=for-the-badge&logo=vim&logoColor=white">
         </td>
    </tr>
    <tr>
        <td style="text-align: center"> Language </td>
        <td>   
            <img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"alt = "HTML5"> 
            <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt = "Pyhton"> 
        </td>
    </tr>
    <tr>
         <td style="text-align: center"> Framework </td> 
         <td> 
             <img src="https://img.shields.io/badge/flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt = "FLASK"> 
         </td>
    </tr>
    <tr>
         <td style="text-align: center"> Protocol </td> 
         <td>  
             <img src="https://img.shields.io/badge/mqtt-02303A?style=for-the-badge&logo=mqtt&logoColor=white" alt ="mqtt">
         </td>
    </tr>
    <tr>
         <td style="text-align: center"> Library/API </td> 
         <td>
         <img src="https://img.shields.io/badge/opencv-F05032?style=for-the-badge&logo=opencv&logoColor=white" alt = "OpenCV">
         </td>
    </tr>
</table>




<table>
    <tbody>
    	<tr>
        	<th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS1.PNG" style="zoom:80%;" alert = "프로젝트 이미지" /></th>
            <th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS.PNG"  style="zoom:80%;" alert = "프로젝트 이미지" /></th>
        </tr>
      	<tr>
        	<th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS2.PNG" style="zoom:80%;"  alert = "프로젝트 이미지" /></th>
            <th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS3.PNG" style="zoom:80%;" alert = "프로젝트 이미지" /></th>
        </tr>
    </tbody>
</table>

### 역할 
---
- 하드웨어 및 소프트웨어 통합 설계
- Flask 및 MQTT를 활용하여 각종 데이터 실시간으로 대시보드에 시각화
- 자동 온도 조절 및 pi 카메라를 이용한 CCTV 구현
