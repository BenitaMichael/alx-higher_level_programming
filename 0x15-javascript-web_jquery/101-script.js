'use strict';
$(() => {
  $('DIV#add_item').click(() => {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(() => {
    const lastEle = $('UL.my_list').children().last();
    if (lastEle) {
      lastEle.remove();
    }
  });
  $('DIV#clear_list').click(() => {
    $('UL.my_list').empty();
  });
});
