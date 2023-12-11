// var mapContainer = document.getElementById('mapbox'), // 지도를 표시할 div 
//     mapOption = { 
//         center: new kakao.maps.LatLng(35.846410, 127.132560), // 지도의 중심좌표
//         level: 3 // 지도의 확대 레벨
//     };

// var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// // 마커가 표시될 위치입니다 
// var markerPosition  = new kakao.maps.LatLng(35.846330, 127.133428); 

// // 마커를 생성합니다
// var marker = new kakao.maps.Marker({
//     position: markerPosition
// });

// // 마커가 지도 위에 표시되도록 설정합니다
// marker.setMap(map);

// // 아래 코드는 지도 위의 마커를 제거하는 코드입니다
// // marker.setMap(null); 


var map;
var markers = []; // 현재 지도에 표시된 마커들을 추적

// 맵 초기화
function initializeMap() {
        var mapContainer = document.getElementById('mapbox'), // 지도를 표시할 div
            mapOption = {
                center: new kakao.maps.LatLng(35.846410, 127.132560), // 지도의 중심좌표
                level: 4 // 지도의 확대 레벨
            };

        // 지도를 생성합니다
        map = new kakao.maps.Map(mapContainer, mapOption);
        mapContainer.style.height = '500px'; 
    }

function placeMarker(y_value, x_value) {
    // 기존 마커 제거
    markers.forEach(function(marker) {
        marker.setMap(null);
    });
    markers = [];

    var markposition = new kakao.maps.LatLng(y_value, x_value);

    // 마커를 생성합니다
    var marker = new kakao.maps.Marker({
        position: markposition
    });

    // 생성된 마커를 지도에 표시합니다
    marker.setMap(map);
    markers.push(marker); // 마커 추적을 위해 배열에 추가

    // 지도의 중심을 마커의 위치로 이동시킵니다
    map.setCenter(markposition);
}


    // 페이지 로드 시 맵 초기화
    window.onload = function() {
        initializeMap();
    };



const clearInput = () => {
    const input = document.getElementsByTagName("input")[0];
    input.value = "";
    markers.forEach(function(marker) {
        marker.setMap(null);
    });
    markers = [];
  }
  
const clearBtn = document.getElementById("clear-btn");
clearBtn.addEventListener("click", clearInput);
  
  