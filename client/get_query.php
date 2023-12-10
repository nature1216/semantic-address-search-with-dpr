<?php
if (isset($_GET['dpr_query'])) {
    $query = $_GET['dpr_query'];
    // 필요한 작업 수행
    echo "검색 쿼리: " . htmlspecialchars($query);
} else {
    echo "검색 쿼리가 제공되지 않았습니다.";
}
?>
