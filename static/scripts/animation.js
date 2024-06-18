(function () {
    var graph = document.querySelector('.right_side__graph');
    var columns = graph.querySelectorAll('.graph__column___box');
    graph.querySelector('.graph__column___animation260').classList.remove('graph__column___animation260');
    graph.querySelector('.graph__column___animation244').classList.remove('graph__column___animation244');
    graph.querySelector('.graph__column___animation251').classList.remove('graph__column___animation251');

    var observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
        if (typeof getCurrentAnimationPreference === 'function' && !getCurrentAnimationPreference()) {
        return;
        }

        if (entry.isIntersecting) {
            columns[0].classList.add('graph__column___animation260');
            columns[1].classList.add('graph__column___animation244');
            columns[2].classList.add('graph__column___animation251');
        return;
        }

        columns[0].classList.remove('graph__column___animation260');
        columns[1].classList.remove('graph__column___animation244');
        columns[2].classList.remove('graph__column___animation251');
    });
    });

    observer.observe(graph);
})();
(function () {
    var block = document.querySelector('.course_block__right_side');
    block.classList.remove('course_block__right_side-animation');
  
    var observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (typeof getCurrentAnimationPreference === 'function' && !getCurrentAnimationPreference()) {
          return;
        }
  
        if (entry.isIntersecting) {
            block.classList.add('course_block__right_side-animation');
          return;
        }
  
        block.classList.remove('course_block__right_side-animation');
      });
    });
  
    observer.observe(block);
  })();