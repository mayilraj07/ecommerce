const uname = document.getElementById('username')
const pwd = document.getElementById('password')
const form = document.getElementById('login-form')

if(form !== null){
  form.addEventListener('submit',(e) =>{
    if(isValidate()){
      e.preventDefault();
    }
    
  })
  function isValidate(){
    const userName = uname.value.trim()
    const password = pwd.value.trim()
    let error = false
  
    if(userName === ''){
      setError(uname,'User name Required')
      error = true;
    }
    else{
      setSuccess(uname,'')
    }
  
    if(password === ''){
      setError(pwd,'Password Required')
      error = true;
    }
    else{
      setSuccess(pwd,'')
    }
    return error
    
  }
  
}

const userName = document.getElementById('id_username')
const email = document.getElementById('id_email')
const pwd1 = document.getElementById('id_password1')
const pwd2 = document.getElementById('id_password2')
const regbtn = document.getElementById('regbtn')
if(regbtn !== null){
  
  regbtn.addEventListener('click',(e) => {
      if(isValidForm()){
        
          e.preventDefault();
      }
  })
  function isValidForm(){
      const user = userName.value.trim()
      const emailVal = email.value.trim()
      const password1 = pwd1.value.trim()
      const password2 = pwd2.value.trim()
      let error = false;

      if(user === ""){
          setError(userName,'* Please fill out this field')
          error = true
      }
      else if(!isNaN(user)){
          setError(userName,'* Please fill out this field')
          error = true
      }
      else if(!nameValidate(user)){
          setError(userName,'* Only Alphabets letters Allowed')
          error = true
      }
      else if(user.length > 10 || user.length < 3){
          setError(userName,'* Minimum 3 and Maximum 10 Characters Allowed')
          error = true
      }
      else{
          setSuccess(userName,'')
      }
      if(emailVal === ""){
          setError(email,"* Please fill out this field");
          error = true;
      }
      else if(!validEmail(emailVal)){
          setError(email,"* Please enter the valid email")
          error = true;
      }
      else{
          setSuccess(email,'')
          
      }
      if(password1 === ""){
          setError(pwd1,"* Please fill out this field")
          error = true;
      }
      else if(!checkPassword(password1)){
          setError(pwd1,"* Password is 8 to 15 characters which contain at least one lowercase letter, one uppercase letter, one numeric digit, and one special character");
          error = true;
      }
      else{
          setSuccess(pwd1,"")
        }
    
      if(password2 === ""){
          setError(pwd2,"* Please fill out this field")
          error = true;
      }
      else if(password2 !== password1){
          setError(pwd2,"* Password does not match please enter correct password")
          error = true;
      }
      else{
          setSuccess(pwd2,'')
        
      }
      return error
  }
}

function nameValidate(name){
    var nameval = /^[A-Za-z]+$/;
    if(nameval.test(name)){
        return true
    }
    else{
        return false
    }
}

function validEmail(mail){
    const checkEmail = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    // const emailVal = /^([a-zA-Z0-9_\.\-])+\@(([a-zA-Z0-9\-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    if(mail.match(checkEmail)){
        return true;
    }
    else{
        return false;
    }
}

function checkPassword(password){
    const passcode=  /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?!.*\s).{8,15}$/;
    if(password.match(passcode)){
        return true;
    }
    else {
        return false;
    }
}

function setError(element,message){
    const pElement =element.parentElement;
    const errorElement = pElement.querySelector('#error');
    result = errorElement.innerHTML = message;
    pElement.classList.add('error');
    pElement.classList.remove('success')
}
function setSuccess(element,message){
    const pElement =element.parentElement;
    const errorElement = pElement.querySelector('#error');
    result = errorElement.innerHTML = message;
    pElement.classList.add('success');
    pElement.classList.remove('error')
}

