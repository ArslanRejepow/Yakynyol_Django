var tet=document.getElementById('tet');
var text=document.getElementById('textfield')

id=Math.round(Math.random()*(inlisceler.length-1));
tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:yellow'><p>"+turkmenceler[id]+" <br> "+gosmaca1[id]+"</p></div></div></div></div>";


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
    tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group' onclick=playbyid("+inlisceler2.indexOf(inlisceler[id])+") style='cursor:pointer'><div class='text' style='background-color:yellow'><p>"+turkmenceler[id]+" <br> "+gosmaca1[id]+"</p></div></div></div></div>";
    tet.scrollTop=tet.scrollHeight;
    aytdyr();
}

function jogapbarla() {
    gelenjogap=text.value.replaceAll('\n','');
    gelenjogap=gelenjogap.replaceAll(' ','');
    dogryjogap=inlisceler[id];
    dogryjogap=dogryjogap.replaceAll(' ','');
    if (gelenjogap.toLowerCase()==dogryjogap.toLowerCase()) {
        setTimeout(dogrygorkez,1000);
        setTimeout(soragber,5000);
    }else{
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:red;color:white'><p><p style='font-size:30px'>&#9785;</p>Ýalňyşdyňyz!!! Dogrusy:  "+inlisceler[id]+"</p></div></div></div></div>";
        tet.scrollTop=tet.scrollHeight;
    }
}


function arassala(){
    inlisceler.splice(id,1);
    turkmenceler.splice(id,1);
    dogrytext.splice(id,1);
    music.splice(id,1);
    gosmaca1.splice(id,1);
    aydym.splice(id,1);
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
        for (var i of music2){
            music.push(i);
        }
        for (var i of aydym2){
            aydym.push(i);
        }
    }
}

function dogrygorkez() {
    if (turkmenceler2.indexOf(turkmenceler[id])%2==0){
        idd = turkmenceler2.indexOf(turkmenceler[id]) + 1;
        console.log(turkmenceler2[idd]);
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:green;color:white'><p><p style='font-size:30px'>&#128077;("+turkmenceler[id]+")  </p>      "+gosmaca1[id]+"<br> Jogaby:  "+turkmenceler2[idd]+'<br>'+gosmaca12[idd]+'<br>'+inlisceler2[idd]+"</p></div></div></div></div>";
        tet.scrollTop=tet.scrollHeight;
    }else{
        idd = turkmenceler2.indexOf(turkmenceler[id]) - 1;
        console.log(turkmenceler2[idd]);
        tet.innerHTML=tet.innerHTML+"<div class='message'><img class='avatar-md' src='dist/img/avatars/avatar-female-5.jpg' data-toggle='tooltip' data-placement='top' title='Keith' alt='avatar'><div class='text-main'><div class='text-group'><div class='text' style='background-color:green;color:white'><p><p style='font-size:30px'>&#128077;("+turkmenceler[id]+")  </p>      "+gosmaca1[id]+"<br> Soragy:  "+turkmenceler2[idd]+'<br>'+gosmaca12[idd]+'<br>'+inlisceler2[idd]+"</p></div></div></div></div>";
        tet.scrollTop=tet.scrollHeight;
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

function aytdyr2() {
    var src=document.getElementById('src');
    var y=document.getElementById('y');
    if(music[id][6]==' '){
        music[id] = music[id].replace(' ','');
        console.log(music[id]);
    }
    src.src=music[id];
    y.load();
    console.log(y.duration);
    y.play();
}
function aytdyr() {
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
    if(aydym2[n][6]==' '){
        aydym2[n] = aydym2[n].replace(' ','');
        console.log(aydym2[n]);
    }
    src.src=aydym2[n];
    y.load();
    y.play();
    console.log(n);
}
