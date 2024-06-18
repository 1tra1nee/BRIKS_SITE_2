function nav_main(hrf) {

 document.write('<div class="nav-scroller">');
 document.write('<nav class="nav-scroller__items dragscroll">');

 if(hrf=="main") {
   document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Главная</a>');
   }
 else {
  document.write('<a href="/" class="nav-scroller__item">Главная</a>');
 }
  if(hrf=="teachers") {
   document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Наши специалисты</a>');
  }
  else {
   document.write('<a href="/teachers" class="nav-scroller__item">Наши специалисты</a>');
 }
  if(hrf=="disciplines") {
    document.write(' <a href="#" class="nav-scroller__item nav-scroller__item_active">Направления</a>');
   }
  else {
   document.write(' <a href="/disciplines" class="nav-scroller__item">Направления</a>');
  }
  if(hrf=="materials") {
     document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Литература</a>');
   }
   else {
   document.write('<a href="/materials" class="nav-scroller__item">Литература</a>');
  }
    if(hrf=="abitur") {
      document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">О группах</a>');
     }
    else {
    document.write('<a href="/abitur" class="nav-scroller__item">О группах</a>');
    }
      if(hrf=="science") {
       document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Наука</a>');
      }
      else {
       document.write('<a href="/science" class="nav-scroller__item">История</a>');
     }
      if(hrf=="contacts") {
          document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active">Контакты</a>');
       }
       else {
       document.write('<a href="/contacts" class="nav-scroller__item">Адреса</a>');
       }
      if(hrf=="loginMe") {
         document.write('<a href="#" class="nav-scroller__item nav-scroller__item_active>Регистрация</a>');
         }
      /*else {
         document.write('<a href="/contacts" class="nav-scroller__item">Войти</a>');
         document.write('<a href="/contacts" class="nav-scroller__item">Регистрация</a>');
         }*/
 document.write('</nav>');
 document.write('</div>');
}
