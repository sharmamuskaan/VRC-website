function show(){
    document.getElementById('sidebar').classList.toggle('active');
}

const burger =  document.querySelector('.toggle-btn');

burger.addEventListener('click', ()=>{
    burger.classList.toggle('cross');
})


navlinks = document.getElementsByTagName('li');

for(var i=0;i<navlinks.length;i++){
navlinks[i].addEventListener("click",function(){
    var linkInnerText = this.innerText;
    switch (linkInnerText) {
        case " | Home":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | About":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | Education":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | Books":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | Awards":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | Achievements":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | Interactions":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        case " | Contact":
            document.getElementById('sidebar').classList.toggle('active');
            burger.classList.toggle('cross');
            break;
        default:
            break;
    }
});
}

/*
buttons = document.getElementsByClassName('btnctn');
paras = document.getElementsByClassName('interPara');

var i;
for(i=1; i<paras.length; i++)
{
paras[i].classList.add('hideIt');
}

for(i=0; i<buttons.length; i++)
{

buttons[i].addEventListener('click', function(){
   var j;
   paras = document.getElementsByClassName('interPara');
   buttons = document.getElementsByClassName('btnctn');

    console.log(paras.length)

   for(j=0; j<paras.length; j++)
   {

    document.getElementsByClassName('interPara')[j].classList.add('hideIt');
   }
    document.getElementsByClassName('interPara')[i].classList.remove('hideIt');
    document.getElementsByClassName('interPara')[i].classList.add('visible');
})
}*/



function getToken(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== "") {
          var cookies = document.cookie.split(";");
          for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === name + "=") {
              cookieValue = decodeURIComponent(
                cookie.substring(name.length + 1)
              );
              break;
            }
          }
        }
        return cookieValue;
      }
      var csrftoken = getToken("csrftoken");



var interBtns = document.getElementsByClassName('inter');
console.log(interBtns);

for (var i = 0; i < interBtns.length; i++) {
  interBtns[i].addEventListener("click", function () {
    var category = this.dataset.category;

    updateInteraction(category);
    });
 }

 function updateInteraction(category)
 {
     console.log(category);

   url = '/update-interaction/';

   fetch(url, {
    method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({'category':category})
    })

    .then((response)=> {
        return response.json()
    })


    .then((data)=> {
    console.log("data:", data);
    document.getElementById('interPara').innerHTML = data;
 })
}

document.getElementsByClassName("popup")[0].classList.add("hide");

achbuttons=document.getElementsByClassName("btn-outline-secondary");
for(var i=0;i<achbuttons.length;i++){
   achbuttons[i].addEventListener("click",function(){

        var category = this.dataset.category;
        console.log(category);

        url = '/update-achievement/'

        fetch(url, {
        method:'POST',
        headers:{
        'Content-Type':'application/json',
        'X-CSRFToken': csrftoken
        },
        body:JSON.stringify({'category':category})
        })
        .then((response)=> response.json())

        .then((data)=> {
        document.getElementsByClassName("popup")[0].classList.remove("hide")
        document.getElementsByClassName("popup")[0].innerHTML=data

       } )




});
}