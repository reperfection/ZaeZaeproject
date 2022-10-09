let elIu = document.querySelector("#username");
let elIp = document.querySelector("#pw");
let elIPr = document.querySelector("#pw-retype");
let elNt = document.querySelector("#phonenumber");
let elJb = document.querySelector("#joinbutton");

let elFm = document.querySelector(".failure-message");
let elSm = document.querySelector(".success-message");
let elMMm = document.querySelector(".mismatch-message");
let elMm = document.querySelector(".match-message");
let elMNm = document.querySelector(".misnumber-message");

elJb.disabled = true;

elIu.onkeyup = function () {
  if (isMoreThan6Length(elIu.value)) {
    elSm.classList.remove("hide");
    elFm.classList.add("hide");
  } else {
    elSm.classList.add("hide");
    elFm.classList.remove("hide");
  }
};

function isMoreThan6Length(value) {
  return value.length >= 6;
}

elIPr.onkeyup = function () {
  if (isMatch(elIp.value, elIPr.value)) {
    elMMm.classList.add("hide");
    elMm.classList.remove("hide");
  } else {
    elMMm.classList.remove("hide");
    elMm.classList.add("hide");
  }
};

function isMatch(pw1, pw2) {
  if (pw1 === pw2) {
    return true;
  } else {
    return false;
  }
}

elNt.onkeyup = function () {
  if (isNumbermatch(elNt.value)) {
    elMNm.classList.add("hide");
  } else {
    elMNm.classList.remove("hide");
  }
};

function isNumbermatch(value) {
  let phonenumber = /^[0-9]*$/;
  if (phonenumber.test(value) === true) {
    return true;
  } else {
    return false;
  }
}

elIu.addEventListener("keyup", button);
elIp.addEventListener("keyup", button);
elIPr.addEventListener("keyup", button);
elNt.addEventListener("keyup", button);

function button() {
  switch (
    !(
      elIu.value &&
      elIp.value &&
      elIPr.value &&
      elNt.value &&
      elIp.value === elIPr.value
    )
  ) {
    case true:
      elJb.disabled = true;
      break;
    case false:
      elJb.disabled = false;
      break;
  }
}
