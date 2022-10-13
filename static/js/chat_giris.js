var tet=document.getElementById('tet');
var text=document.getElementById('textfield')

id=Math.round(Math.random()*(inlisceler.length-1));
tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group' onclick=playbyid("+inlisceler2.indexOf(inlisceler[id])+") style='cursor:pointer' ><div class='text' style='background-color:yellow'><p>"+inlisceler[id]+"</p></div></div></div></div>";


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
    aytdyr();
    tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group' onclick=playbyid("+inlisceler2.indexOf(inlisceler[id])+") style='cursor:pointer'><div class='text' style='background-color:yellow'><p>"+inlisceler[id]+"</p></div></div></div></div>";
    tet.scrollTop=tet.scrollHeight;
}

function jogapbarla() {
    gelenjogap=text.value.replaceAll('\n','');
    gelenjogap=gelenjogap.replaceAll(' ','');
    dogryjogap=inlisceler[id];
    dogryjogap=dogryjogap.replaceAll(' ','');
    console.log(gelenjogap);
    console.log(dogryjogap);
    if (gelenjogap.toLowerCase()==dogryjogap.toLowerCase()) {
        setTimeout(dogrygorkez,1000)
        setTimeout(soragber,3000);                              
    }else{
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:red;color:white'><p><p style='font-size:30px'>&#9785;</p>Ýalňyşdyňyz!!! Dogrusy:  "+inlisceler[id]+"</p></div></div></div></div>";
        tet.scrollTop=tet.scrollHeight;
    }
}


function arassala(){
    inlisceler.splice(id,1);
    turkmenceler.splice(id,1);
    description.splice(id,1);
    music.splice(id,1);
    aydym.splice(id,1);
    gosmaca1.splice(id,1);
    gosmaca3.splice(id,1);
    gosmaca2.splice(id,1);
    console.log(aydym);
    if (inlisceler.length==0) {
        for (var i of inlisceler2){
            inlisceler.push(i);
        }
        for (var i of turkmenceler2){
            turkmenceler.push(i);
        }
        for (var i of description2){
            description.push(i);
        }
        for (var i of music2){
            music.push(i);
        }
        for (var i of aydym2){
            aydym.push(i);
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
    console.log(gosmaca1[id].length);
    if(gosmaca2[id]!=''){
    tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:green;color:white'><p><p style='font-size:30px'>&#128077;"+turkmenceler[id]+' ('+gosmaca1[id]+")   </p>"+gosmaca2[id]+"<br>"+gosmaca3[id]+"<br>"+description[id]+"</p></div></div></div></div>";
    }else{
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:green;color:white'><p><p style='font-size:30px'>&#128077;"+turkmenceler[id]+"   </p>("+description[id]+"<br>"+gosmaca1[id]+")</p></div></div></div></div>";
    }
    tet.scrollTop=tet.scrollHeight;
    aytdyr2();
}



document.addEventListener('keyup',function(event){
    if(event.keyCode==13){
        tet.innerHTML=tet.innerHTML+"<div class='message me'><div class='text-main'><div class='text-group me'><div class='text me'><p>"+text.value+"</p></div></div></div></div>"; 
        jogapbarla();
        text.value='';
    }

})

function aytdyr() {
    var src=document.getElementById('src');
    var y=document.getElementById('y');
    console.log(music[id]);
    if(music[id][6]==' '){
        music[id] = music[id].replace(' ','');
        console.log(music[id]);
    }
    src.src=music[id];
    y.load();
    y.play();
}
function aytdyr2() {
    var src=document.getElementById('src');
    var y=document.getElementById('y');
    if(aydym[id][6]==' '){
        aydym[id] = aydym[id].replace(' ','');
        console.log(aydym[id]);
    }
    src.src=aydym[id];
    y.load();
    y.play();
}

function playbyid(n){
    var src=document.getElementById('src');
    var y=document.getElementById('y');
    if(music2[n][6]==' '){
        music2[n] = music2[n].replace(' ','');
        console.log(music2[n]);
    }    src.src=music2[n];
    y.load();
    y.play();
    console.log(n);
}
