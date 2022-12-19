$(document).ready(function() {
  $("#add_item").click(()=>{ $('.my_list').append("<li>Item</li>") })
  $("#remove_item").click(()=>{ $('ul li').last().remove() })
  $("#clear_list").click(()=>{ $('li').remove() })
});
