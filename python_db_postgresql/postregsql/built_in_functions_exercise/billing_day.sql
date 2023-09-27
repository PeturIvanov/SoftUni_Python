ALTER TABLE bookings
ADD COLUMN billing_day TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP;

SELECT
	concat_ws(' ',
						to_char(billing_day, 'DD'),
						'Day',
						to_char(billing_day, 'MM'),
						'Month',
						to_char(billing_day, 'YYYY'),
						'Year',
						to_char(billing_day, 'HH24:MI:SS')
					 ) AS "Billing Day"
FROM
	bookings
ORDER BY billing_day