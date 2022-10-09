let idUserName = document.querySelector("#id_username");
let idPw = document.querySelector("#id_password1");

if (idUserName.value == "") {
  alert("아이디를 입력하세요");
  idUserName.focus();
  return false;
}

if (idPw.value == "") {
  alert("비밀번호를 입력하세요");
  idPw.focus();
  return false;
}

let idPwCheck = /^(?=.*[a-zA-Z])(?=.*[!@#$%^*+=-])(?=.*[0-9]).{8,25}$/;

if (!idPwCheck.test(idPw.value)) {
  alert("비밀번호는 영문자+숫자+특수문자 조합으로 8~25자리를 사용해야 합니다.");
  idPw.focus();
  return false;
}
