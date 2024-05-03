// scripts.js
document.addEventListener('DOMContentLoaded', function () {
    const sidenav = document.getElementById('sidenav');
    const mainBody = document.getElementById('mainBody');
    const btnClose = document.getElementById('btnClose');

    btnClose.addEventListener('click', function () {
        sidenav.classList.toggle('sidenav-collapsed');
        mainBody.classList.toggle('body-empty');
    });
});
