

list=document.getElementsByTagName('input');
for(let i of list){
    if(i.type=='radio' && (i.value.split('_')[3]=='1')){
        i.checked=true;
    };
    
};
