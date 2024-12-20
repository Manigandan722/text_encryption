function performAffineCipher() {
  // Get input values from form
  var plaintext = $('#plaintext').val();
  var keyA = parseInt($('#keyA').val());
  var keyB = parseInt($('#keyB').val());
  var operation = $('#operation').val();

  // Send data to server for processing
  $.ajax({
    url: '/affine',
    type: 'POST',
    data: {
      plaintext: plaintext,
      key_a: keyA,
      key_b: keyB,
      operation: operation
    },
    success: function(result) {
      // Update result element with ciphertext or plaintext
      $('#result').text(result);
    }
  });
}
