const checkbtnTag = document.querySelector('.shared-switch');

checkbtnTag.addEventListener('change', function() {
    // 체크 박스가 변경될 때 호출되는 함수
    const isChecked = this.checked; // 체크 박스가 체크되었는지 여부 확인

    // isChecked 값에 따라 check_share 값을 토글
    if (isChecked) {
        check_share = false;
    } else {
        check_share = true;
    }
})