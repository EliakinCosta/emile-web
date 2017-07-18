var helpers =
{
    buildDropdown: function(result, dropdown, emptyMessage, key, value)
    {
        // Remove current options
        dropdown.html('');
        // Add the empty option with the empty message
        dropdown.append('<option value="">' + emptyMessage + '</option>');
        // Check result isnt empty
        console.log(result)
        console.log(dropdown)
        console.log(emptyMessage)
        if(result != '')
        {
            // Loop through each of the results and append the option to the dropdown
            $.each(result, function(k, v) {
                dropdown.append('<option value="' + v[key] + '">' + v[value] + '</option>');
            });
        }
    },
    findTypeDestination: function(dataList, id, callback)
    {
      $.each( dataList, function( index, value ){
        if (value.id == id)
        {
          callback(value);
        }
      });
    }

}
