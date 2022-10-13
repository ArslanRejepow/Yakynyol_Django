var tet=document.getElementById('tet');
var text=document.getElementById('textfield')

id=Math.round(Math.random()*(inlisceler.length-1));
tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:yellow'><p>"+turkmenceler[id]+"<br>"+gosmaca2[id]+"</p></div></div></div></div>";


function jogapla(){
    tet.innerHTML=tet.innerHTML+"<div class='message me'><div class='text-main'><div class='text-group me'><div class='text me'><p>"+text.value+"</p></div></div></div></div>"; 
    jogapbarla();
    tet.scrollTop=tet.scrollHeight;
    text.value='';
}

function soragber(){
    arassala();
    id=Math.round(Math.random()*(inlisceler.length-1));
    // alert(inlisceler.indexOf('hello'));
    tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group' onclick=playbyid("+inlisceler2.indexOf(inlisceler[id])+") style='cursor:pointer'><div class='text' style='background-color:yellow'><p>"+turkmenceler[id]+" <br> "+gosmaca2[id]+"</p></div></div></div></div>";
    tet.scrollTop=tet.scrollHeight;
}

function jogapbarla() {
    gelenjogap=text.value.replace('\n','');
    gelenjogap=gelenjogap.replaceAll(' ','');
    dogryjogap=inlisceler[id];
    dogryjogap=dogryjogap.replaceAll(' ','');
    if (gelenjogap.toLowerCase()==dogryjogap.toLowerCase()) {
        setTimeout(dogrygorkez,1000);
        setTimeout(soragber,3000);
    }else{
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:red;color:white'><p><p style='font-size:30px'>&#9785;</p>Ýalňyşdyňyz!!! Dogrusy:  "+inlisceler[id]+"</p></div></div></div></div>";
        tet.scrollTop=tet.scrollHeight;
    }
}


function arassala(){
    inlisceler.splice(id,1);
    turkmenceler.splice(id,1);
    gosmaca1.splice(id,1);
    gosmaca3.splice(id,1);
    gosmaca2.splice(id,1);
    dogrytext.splice(id,1);
    if (inlisceler.length==0) {
        for (var i of inlisceler2){
            inlisceler.push(i);
        }
        for (var i of turkmenceler2){
            turkmenceler.push(i);
        }
        for (var i of dogrytext2){
            dogrytext.push(i);
        }
        for (var i of gosmaca12){
            gosmaca1.push(i);
        }
        for (var i of gosmaca22){
            gosmaca2.push(i);
        }
        for (var i of gosmaca32){
            gosmaca3.push(i);
        }
    }
}

function dogrygorkez() {
    if(gosmaca2[id]){
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:green;color:white'><p><p style='font-size:30px'>&#128077;"+turkmenceler[id]+' ('+gosmaca1[id]+")   </p>"+gosmaca2[id]+"<br>"+gosmaca3[id]+"<br>"+dogrytext[id]+"</p></div></div></div></div>";
        }else{
            tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:green;color:white'><p><p style='font-size:30px'>&#128077;"+turkmenceler[id]+"   </p>("+dogrytext[id]+"<br>"+gosmaca1[id]+")</p></div></div></div></div>";
        }
        tet.scrollTop=tet.scrollHeight;
}



document.addEventListener('keyup',function(event){
    if(event.keyCode==13){
        tet.innerHTML=tet.innerHTML+"<div class='message me'><div class='text-main'><div class='text-group me'><div class='text me'><p>"+text.value+"</p></div></div></div></div>"; 
        jogapbarla();
        text.value='';
    }

})

