### 버스 모니터링 시스템

> 라즈베리 파이 및 각종 센서를 활용한 IoT 프로젝트

## Description

버스모니터링 시스템은 초음파센서, 온도 센서를 기반으로 버스 내부의 승객의 탑승인원 데이터를 추출하고
FLASK 및 MQTT 통신을 활용해 추출한 데이터를 웹으로 시각화 하는 프로젝트입니다.

초음파 센서 두개를 이용하여 승객의 승하차를 판단하고 온도센서를 통해 자동으로 에어컨을 가동시킵니다(LED로 가정)

시간에 따른 탑승 승객의 수를 파악하게 하여 승객에게 버스 혼잡도를 제공하고, 버스 회사에게 시간에 따른 승객 이용수 데이터를 제공할 수 있습니다.

또한, picamera 와 openCV를 활용해 버스 내부 CCTV를 확인할 수 있습니다.

<table>
    <tbody>
    	<tr>
        	<th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS1.PNG" style="zoom:80%;" /></th>
            <th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS.PNG"  style="zoom:80%;" /></th>
        </tr>
      	<tr>
        	<th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS2.PNG" style="zoom:80%;" /></th>
            <th style="text-align: center"><img src="https://github.com/rloJo/BusMonitoringSystem/blob/main/AssetReadMe/BMS3.PNG" style="zoom:80%;" /></th>
        </tr>
    </tbody>
</table>
