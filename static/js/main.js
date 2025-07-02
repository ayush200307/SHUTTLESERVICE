// Main JavaScript file for Shuttle Management System
$(document).ready(function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Auto-dismiss alerts after 5 seconds
    setTimeout(function() {
        $('.alert').fadeOut('slow');
    }, 5000);

    // Form validation enhancement
    $('form').on('submit', function(e) {
        var form = this;
        var isValid = true;
        
        // Check required fields
        $(form).find('input[required], select[required], textarea[required]').each(function() {
            if (!$(this).val()) {
                $(this).addClass('is-invalid');
                isValid = false;
            } else {
                $(this).removeClass('is-invalid');
            }
        });
        
        // Email validation
        $(form).find('input[type="email"]').each(function() {
            var email = $(this).val();
            var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (email && !emailRegex.test(email)) {
                $(this).addClass('is-invalid');
                isValid = false;
            }
        });
        
        // Phone validation (basic)
        $(form).find('input[type="tel"]').each(function() {
            var phone = $(this).val();
            var phoneRegex = /^[\+]?[0-9\-\(\)\s]+$/;
            if (phone && !phoneRegex.test(phone)) {
                $(this).addClass('is-invalid');
                isValid = false;
            }
        });
        
        if (!isValid) {
            e.preventDefault();
            showAlert('Please fill in all required fields correctly.', 'danger');
        }
    });

    // Clear validation classes on input
    $('input, select, textarea').on('input change', function() {
        $(this).removeClass('is-invalid');
    });

    // Confirm delete actions
    $('.btn-danger[type="submit"]').on('click', function(e) {
        if (!confirm('Are you sure you want to perform this action? This cannot be undone.')) {
            e.preventDefault();
        }
    });

    // Real-time search functionality
    $('.search-input').on('keyup', function() {
        var value = $(this).val().toLowerCase();
        var targetTable = $(this).data('target');
        
        $(targetTable + ' tbody tr').filter(function() {
            $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1);
        });
    });

    // Auto-refresh dashboard statistics
    if (window.location.pathname === '/') {
        setInterval(refreshDashboardStats, 60000); // Refresh every minute
    }

    // Date picker enhancements
    $('input[type="date"]').each(function() {
        if ($(this).attr('min') === undefined) {
            // Set minimum date to today for future bookings
            var today = new Date().toISOString().split('T')[0];
            $(this).attr('min', today);
        }
    });

    // License expiry warning
    checkLicenseExpiry();
});

// Utility function to show alerts
function showAlert(message, type = 'info') {
    var alertHtml = `
        <div class="alert alert-${type} alert-dismissible fade show" role="alert">
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;
    
    // Insert at the top of the main container
    $('.container').first().prepend(alertHtml);
    
    // Auto-dismiss after 5 seconds
    setTimeout(function() {
        $('.alert').first().fadeOut('slow');
    }, 5000);
}

// Function to refresh dashboard statistics
function refreshDashboardStats() {
    $.get('/api/stats')
        .done(function(data) {
            // Update statistics cards if they exist
            if ($('.stats-card').length) {
                console.log('Dashboard stats updated:', data);
                // Update the values in the cards
                // This would require specific selectors for each stat
            }
        })
        .fail(function() {
            console.log('Failed to refresh dashboard statistics');
        });
}

// Function to check for license expiry warnings
function checkLicenseExpiry() {
    $('.license-expiry').each(function() {
        var expiryDate = new Date($(this).text());
        var today = new Date();
        var daysUntilExpiry = Math.ceil((expiryDate - today) / (1000 * 60 * 60 * 24));
        
        if (daysUntilExpiry < 0) {
            $(this).after('<span class="badge bg-danger ms-1">Expired</span>');
        } else if (daysUntilExpiry <= 30) {
            $(this).after('<span class="badge bg-warning ms-1">Expires in ' + daysUntilExpiry + ' days</span>');
        }
    });
}

// Vehicle status update functionality
function updateVehicleStatus(vehicleId, status) {
    $.post('/api/vehicles/' + vehicleId + '/status', {
        status: status
    })
    .done(function() {
        showAlert('Vehicle status updated successfully!', 'success');
        location.reload();
    })
    .fail(function() {
        showAlert('Failed to update vehicle status.', 'danger');
    });
}

// Schedule conflict checking
function checkScheduleConflict(routeId, vehicleId, driverId, departureTime, arrivalTime) {
    // This would make an AJAX call to check for conflicts
    // For now, it's a placeholder function
    return new Promise(function(resolve) {
        // Simulate API call
        setTimeout(function() {
            resolve(false); // No conflict
        }, 500);
    });
}

// Export functionality for reports
function exportToCSV(tableId, filename) {
    var csv = [];
    var rows = document.querySelectorAll(tableId + ' tr');
    
    for (var i = 0; i < rows.length; i++) {
        var row = [], cols = rows[i].querySelectorAll('td, th');
        
        for (var j = 0; j < cols.length - 1; j++) { // Exclude last column (actions)
            row.push(cols[j].innerText);
        }
        
        csv.push(row.join(','));
    }
    
    downloadCSV(csv.join('\n'), filename);
}

function downloadCSV(csv, filename) {
    var csvFile = new Blob([csv], {type: 'text/csv'});
    var downloadLink = document.createElement('a');
    
    downloadLink.download = filename;
    downloadLink.href = window.URL.createObjectURL(csvFile);
    downloadLink.style.display = 'none';
    
    document.body.appendChild(downloadLink);
    downloadLink.click();
    document.body.removeChild(downloadLink);
}

// Print functionality
function printTable(tableId) {
    var printWindow = window.open('', '', 'height=600,width=800');
    var table = document.querySelector(tableId).outerHTML;
    
    printWindow.document.write('<html><head><title>Shuttle Management Report</title>');
    printWindow.document.write('<link href="https://cdn.replit.com/agent/bootstrap-agent-dark-theme.min.css" rel="stylesheet">');
    printWindow.document.write('</head><body>');
    printWindow.document.write('<div class="container mt-4">');
    printWindow.document.write('<h2>Shuttle Management System Report</h2>');
    printWindow.document.write('<p>Generated on: ' + new Date().toLocaleDateString() + '</p>');
    printWindow.document.write(table);
    printWindow.document.write('</div></body></html>');
    
    printWindow.document.close();
    printWindow.print();
}

// Advanced filtering functionality
function initAdvancedFilters() {
    $('.filter-dropdown').on('change', function() {
        var filterValue = $(this).val();
        var filterColumn = $(this).data('column');
        var targetTable = $(this).data('target');
        
        $(targetTable + ' tbody tr').each(function() {
            var cellValue = $(this).find('td').eq(filterColumn).text().toLowerCase();
            
            if (filterValue === '' || cellValue.includes(filterValue.toLowerCase())) {
                $(this).show();
            } else {
                $(this).hide();
            }
        });
    });
}

// Initialize advanced filters when document is ready
$(document).ready(function() {
    initAdvancedFilters();
});
