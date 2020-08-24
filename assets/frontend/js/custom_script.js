// Prevent closing from click inside dropdown
$(document).on('click', '.submenu', function (e) {
    var current=$(this).next();
    current.toggle();
    e.stopPropagation();
});
