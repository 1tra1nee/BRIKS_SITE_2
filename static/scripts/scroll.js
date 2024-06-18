var scrollContainer = document.getElementById("VerticalContainers"); 
    var isMouseDown = false; 
    var startX, scrollLeft;
    
    scrollContainer.addEventListener("mousedown", function(event) { 
        isMouseDown = true; 
        startX = event.clientX;
        scrollLeft = scrollContainer.scrollLeft;  
    }); 
    
    scrollContainer.addEventListener("mouseup", function() { 
        isMouseDown = false; 
    }); 
    
    scrollContainer.addEventListener("mousemove", function(event) { 
        if (!isMouseDown) return; 
        var deltaX = event.clientX - startX; 
        scrollContainer.scrollLeft = scrollLeft - deltaX; 
    });