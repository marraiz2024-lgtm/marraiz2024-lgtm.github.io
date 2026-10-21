(() => {
  'use strict';
  document.documentElement.classList.add('js');
  if(['localhost','127.0.0.1'].includes(location.hostname))import('./diagnostics.js');
  const $=s=>document.querySelector(s), $$=s=>[...document.querySelectorAll(s)];
  const menu=$('#menuToggle'),nav=$('#navigation'),header=$('#header');
  menu.hidden=false;
  const closeMenu=(focus=false)=>{menu.setAttribute('aria-expanded','false');nav.classList.remove('open');menu.innerHTML='Menú <span aria-hidden="true">＋</span>';if(focus)menu.focus();};
  menu.addEventListener('click',()=>{const open=menu.getAttribute('aria-expanded')!=='true';menu.setAttribute('aria-expanded',String(open));nav.classList.toggle('open',open);menu.innerHTML=open?'Cerrar <span aria-hidden="true">−</span>':'Menú <span aria-hidden="true">＋</span>';});
  nav.addEventListener('click',e=>{if(e.target.closest('a'))closeMenu();});
  document.addEventListener('click',e=>{if(!header.contains(e.target))closeMenu();});
  document.addEventListener('keydown',e=>{if(e.key==='Escape'&&nav.classList.contains('open'))closeMenu(true);});
  matchMedia('(min-width:701px)').addEventListener('change',()=>closeMenu());
  const messages={morning:['Exacto: Good morning.','«Buenos días» es el saludo que usamos por la mañana. Ahora imagina que llegas a clase: Good morning, Ana.'],night:['En esta situación, usa Good morning.','Good night se usa al despedirse por la noche o antes de dormir. Para saludar al llegar por la mañana, di Good morning.'],evening:['Fíjate en la hora: es por la mañana.','Good evening es un saludo para la tarde-noche. Aquí corresponde Good morning: «Buenos días».']};
  $$('.answer').forEach(b=>b.addEventListener('click',()=>{ $$('.answer').forEach(x=>x.setAttribute('aria-pressed',String(x===b)));const [title,body]=messages[b.dataset.answer];const strong=document.createElement('strong'),span=document.createElement('span');strong.textContent=title;span.textContent=body;$('#lessonFeedback').replaceChildren(strong,span);}));
  $('#translationToggle').addEventListener('click',()=>{const open=$('#translation').hidden;$('#translation').hidden=!open;$('#translationToggle').setAttribute('aria-expanded',String(open));$('#translationToggle').textContent=open?'Ocultar traducción':'Mostrar traducción';});
  $('#lessonReset').addEventListener('click',()=>{$$('.answer').forEach(b=>b.setAttribute('aria-pressed','false'));$('#lessonFeedback').textContent='Piensa en el momento del día antes de elegir.';$('#translation').hidden=true;$('#translationToggle').setAttribute('aria-expanded','false');$('#translationToggle').textContent='Mostrar traducción';$('.answer').focus();});
  $('#newsletterForm').addEventListener('submit',()=>{if($('#newsletterForm').checkValidity())$('#newsletterStatus').textContent='Continúa en la pestaña de Brevo para conocer el resultado de tu solicitud. La suscripción todavía no está confirmada aquí.';});
  const form=$('#conversation'),fields=$$('[data-step]'),name=$('#firstName'),objective=$('#objective');
  let step=0;
  form.noValidate=true;
  function showStep(){fields.forEach((x,i)=>x.hidden=i!==step);$('#formStepText').textContent=`Paso ${step+1} de 3`;$('#formProgress').value=step+1;$('#formBack').hidden=step===0;$('#formNext').textContent=step===2?'Preparar consulta →':'Continuar →';$('#formError').textContent='';fields[step].querySelector('input,textarea').focus();}
  function valid(){const control=step===0?name:step===2?objective:fields[1].querySelector('input');const okay=step===0?name.value.trim():step===2?objective.value.trim():$('input[name=nivel]:checked');$$('[aria-invalid]').forEach(x=>{x.removeAttribute('aria-invalid');x.removeAttribute('aria-describedby');});if(!okay){$('#formError').textContent=step===0?'Escribe tu nombre para continuar.':step===1?'Elige la opción que mejor describe tu punto de partida.':'Cuéntame brevemente qué te gustaría lograr.';control.setAttribute('aria-invalid','true');control.setAttribute('aria-describedby','formError');control.focus();return false;}return true;}
  form.addEventListener('submit',e=>{e.preventDefault();if(!valid())return;if(step<2){step++;showStep();return;}const level=$('input[name=nivel]:checked').value;const message=`Hola, Mercedes. Soy ${name.value.trim()}.\n\nMi punto de partida: ${level}.\nMi objetivo: ${objective.value.trim()}\n\nQuiero confirmar mi nivel, elegir la modalidad y acordar un horario para las clases en vivo por Zoom.`;$('#messagePreview').textContent=message;$('#whatsappMessage').href='https://wa.me/19044266634?text='+encodeURIComponent(message);form.hidden=true;$('#formReview').hidden=false;$('#copyStatus').textContent='';$('#reviewTitle').focus();});
  $('#formBack').addEventListener('click',()=>{if(step>0){step--;showStep();}});
  $('#editMessage').addEventListener('click',()=>{form.hidden=false;$('#formReview').hidden=true;step=0;showStep();});
  $('#copyMessage').addEventListener('click',async()=>{try{await navigator.clipboard.writeText($('#messagePreview').textContent);$('#copyStatus').textContent='Mensaje copiado. No se ha enviado.';}catch{const range=document.createRange();range.selectNodeContents($('#messagePreview'));const selection=getSelection();selection.removeAllRanges();selection.addRange(range);$('#copyStatus').textContent='El mensaje está seleccionado. Usa la opción Copiar de tu dispositivo.';}});
  // The privacy anchor opens its disclosure for both mouse and keyboard navigation.
  function openPrivacy(){if(location.hash==='#privacidad')$('#privacidad').open=true;}
  addEventListener('hashchange',openPrivacy);openPrivacy();
  const reduced=matchMedia('(prefers-reduced-motion:reduce)'),saveData=navigator.connection?.saveData,params=new URLSearchParams(location.search);
  const requestedReduced=params.get('movimiento')==='reducido';
  if(requestedReduced)document.documentElement.classList.add('reduced-motion');
  if(!reduced.matches&&!requestedReduced&&!saveData&&!params.has('sin3d')){
    const start=()=>import('./assets/scene.js').catch(()=>{/* Static illustration remains visible. */});
    if('requestIdleCallback'in window)requestIdleCallback(start,{timeout:2500});else setTimeout(start,1000);
  }
})();
