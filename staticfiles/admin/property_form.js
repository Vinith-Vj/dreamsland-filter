document.addEventListener('DOMContentLoaded', function() {
    function toggleFields() {
        const propertyType = document.getElementById('id_property_type');
        const propertySubtype = document.getElementById('id_property_subtype');

        const bhkRow = document.querySelector('.form-row.field-bhk');
        const squareFeetRow = document.querySelector('.form-row.field-square_feet');

        if (!propertyType || !propertySubtype) return;

        if (propertyType.value === 'residential' && propertySubtype.value === 'residential_land') {
            if (bhkRow) bhkRow.style.display = 'none';
            if (squareFeetRow) squareFeetRow.style.display = 'none';
        } else {
            if (bhkRow) bhkRow.style.display = '';
            if (squareFeetRow) squareFeetRow.style.display = '';
        }
    }

    const propertyType = document.getElementById('id_property_type');
    const propertySubtype = document.getElementById('id_property_subtype');

    if (propertyType) {
        propertyType.addEventListener('change', toggleFields);
    }

    if (propertySubtype) {
        propertySubtype.addEventListener('change', toggleFields);
    }

    // Run on page load to handle pre-filled data (like Edit page)
    toggleFields();
});
