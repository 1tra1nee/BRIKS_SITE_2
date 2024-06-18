document.addEventListener('DOMContentLoaded', function() {
    var parentElements = document.querySelectorAll('.parent-element');
    
    parentElements.forEach(function(parentElement) {
        parentElement.addEventListener('mouseover', function() {
            var icon = parentElement.querySelector('dotlottie-player');
            
            if (icon.getState()['currentState'] == 'completed') {
                icon.stop();
            }
            icon.play();
        });
    });
});