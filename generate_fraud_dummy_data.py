#!/usr/bin/env python3
"""
Fraud Prevention System Dummy Data Generator

This script generates 1000 rows of realistic dummy data for fraud prevention 
system reporting. The data includes device fingerprints, risk scores, account 
information, geographic data, payment details, and various fraud indicators.

Author: Generated for terraform-practice-2025 repository
"""

import csv
import random
import string
import hashlib
from datetime import datetime, timedelta
from faker import Faker
import uuid

# Initialize Faker for realistic data generation
fake = Faker()

def generate_device_fingerprint():
    """Generate a realistic device fingerprint hash"""
    # Create a pseudo-device fingerprint using common browser/device characteristics
    characteristics = [
        fake.user_agent(),
        str(random.randint(1024, 3840)),  # Screen width
        str(random.randint(768, 2160)),   # Screen height
        str(random.randint(8, 64)),       # Color depth
        fake.timezone()
    ]
    fingerprint_string = '|'.join(characteristics)
    return hashlib.md5(fingerprint_string.encode()).hexdigest()

def generate_device_score():
    """Generate device-related risk scores (0-1000 scale)"""
    return random.randint(0, 1000)

def generate_risk_rating():
    """Generate TMX risk rating (typically LOW, MEDIUM, HIGH, REVIEW)"""
    return random.choice(['LOW', 'MEDIUM', 'HIGH', 'REVIEW', 'TRUSTED'])

def generate_email_score():
    """Generate email risk score (0-999 range typical for fraud systems)"""
    return random.randint(0, 999)

def generate_reason_code():
    """Generate TMX reason codes (typical fraud system codes)"""
    codes = ['BROWSER_LANGUAGE', 'SCREEN_RESOLUTION', 'TIMEZONE_MISMATCH', 
             'DEVICE_VELOCITY', 'IP_GEOLOCATION', 'SUSPICIOUS_ACTIVITY',
             'CLEAN', 'REVIEW_REQUIRED', 'HIGH_RISK_COUNTRY']
    return random.choice(codes)

def generate_datetime_string():
    """Generate realistic datetime string for fraud system"""
    # Generate dates within the last 2 years
    start_date = datetime.now() - timedelta(days=730)
    end_date = datetime.now()
    random_date = fake.date_time_between(start_date=start_date, end_date=end_date)
    return random_date.strftime('%Y-%m-%d %H:%M:%S')

def generate_assert_history():
    """Generate assertion history code (typical values for fraud systems)"""
    histories = ['FIRST_TIME', 'PREVIOUSLY_SEEN', 'FREQUENT', 'SUSPICIOUS', 
                'WHITELIST', 'BLACKLIST', 'UNKNOWN', 'VERIFIED']
    return random.choice(histories)

def generate_ip_address():
    """Generate realistic IP address"""
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_card_hash():
    """Generate anonymized credit card hash"""
    # Simulate PCI-compliant card number hashing
    fake_card = fake.credit_card_number()
    return hashlib.sha256(fake_card.encode()).hexdigest()[:16]

def generate_device_id():
    """Generate device ID (typically UUID-like for fraud systems)"""
    return str(uuid.uuid4())

def generate_fuzzy_device_id():
    """Generate fuzzy device ID for device linking"""
    return f"FZ_{random.randint(100000, 999999)}"

def generate_ea_score():
    """Generate Email Address (EA) risk score"""
    return random.randint(0, 100)

def generate_domain_risk():
    """Generate domain risk level"""
    return random.choice(['LOW', 'MEDIUM', 'HIGH', 'UNKNOWN'])

def generate_country_code():
    """Generate realistic country code"""
    return fake.country_code()

def generate_phone_number():
    """Generate realistic phone number"""
    return fake.phone_number()

def generate_amount():
    """Generate transaction amount (realistic for e-commerce)"""
    return round(random.uniform(10.00, 5000.00), 2)

def generate_status_code():
    """Generate fraud status codes"""
    return random.choice(['ACCEPT', 'REJECT', 'REVIEW', 'PENDING', 'MANUAL_REVIEW'])

def generate_bin():
    """Generate Bank Identification Number (first 6 digits of card)"""
    return str(random.randint(400000, 599999))  # Typical Visa/MC ranges

def generate_cvv_match():
    """Generate CVV match result"""
    return random.choice(['Y', 'N', 'U', 'P'])  # Yes, No, Unavailable, Not Processed

def generate_avs_match():
    """Generate AVS (Address Verification Service) match result"""
    return random.choice(['Y', 'N', 'A', 'Z', 'U', 'R'])

def generate_row():
    """Generate a single row of fraud prevention dummy data"""
    
    # Generate base values that might be referenced multiple times
    device_fp = generate_device_fingerprint()
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    city = fake.city()
    state = fake.state_abbr()
    country = generate_country_code()
    ip_addr = generate_ip_address()
    created_date = generate_datetime_string()
    
    return {
        # Device and fingerprint data
        'DEVICE_FINGERPRINT': device_fp,
        'DEVICE_FINGERPRINT_SCORE': generate_device_score(),
        'TMX_RISK_RATING': generate_risk_rating(),
        
        # Account scoring
        'ACCOUNT_EMAIL_SCORE': generate_email_score(),
        'ACCOUNT_TELEPHONE_SCORE': generate_email_score(),
        'SMART_LEARNING_FRAUD_RATING': generate_risk_rating(),
        'SMART_LEARNING_RISK_RANK': random.randint(1, 100),
        'TMX_REASON_CODE': generate_reason_code(),
        
        # Account history and scoring
        'ACCOUNT_LOGIN_FIRST_SEEN': generate_datetime_string(),
        'ACCOUNT_LOGIN_SCORE': generate_device_score(),
        'ACCOUNT_NAME_SCORE': generate_email_score(),
        
        # Assertion histories
        'CC_NUMBER_HASH_ASSERT_HISTORY': generate_assert_history(),
        'DEVICE_ASSERT_HISTORY': generate_assert_history(),
        'DEVICE_FINGERPRINT_ASSERT_HISTORY': generate_assert_history(),
        'SHIPPING_ADDRESS_ASSERT_HISTORY': generate_assert_history(),
        'true_ip_assert_history': generate_assert_history(),
        
        # Review and scoring
        'FINAL_REVIEW_STATUS': generate_status_code(),
        'SHIPPING_ADDRESS_SCORE': generate_email_score(),
        'TMX_POLICY_SCORE': generate_device_score(),
        'TMX_SUMMARY_REASON_CODE': generate_reason_code(),
        
        # Device tracking
        'device_id': generate_device_id(),
        'device_first_seen': generate_datetime_string(),
        'device_score': generate_device_score(),
        'fuzzy_device_id': generate_fuzzy_device_id(),
        'fuzzy_device_score': generate_device_score(),
        'device_id_confidence': random.randint(0, 100),
        
        # Policy and risk
        'policy_score': generate_device_score(),
        'reason_code': generate_reason_code(),
        'request_result': generate_status_code(),
        'risk_rating': generate_risk_rating(),
        'digital_id_trust_score_rating': generate_risk_rating(),
        
        # Geographic data
        'true_ip_city': city,
        'ip_city': city,
        'ip_countryCode': country,
        'ip_region': state,
        
        # Email analysis (EA) data
        'ea_advice_id': random.randint(1000, 9999),
        'ea_reason': random.choice(['DOMAIN_RISK', 'AGE_RISK', 'REPUTATION', 'CLEAN']),
        'ea_reason_id': random.randint(100, 999),
        'ea_risk_band_id': random.randint(1, 5),
        'ea_score': generate_ea_score(),
        'ea_status_id': random.randint(1, 10),
        
        # Domain analysis
        'domain_exists': random.choice(['Y', 'N']),
        'domaincorporate': random.choice(['Y', 'N']),
        'domainrelevantinfoID': random.randint(1, 100),
        'domainrisklevel': generate_domain_risk(),
        'domainrisklevelID': random.randint(1, 4),
        
        # Core customer data
        'email': email,
        'email_age': random.randint(1, 3650),  # Days since email creation
        'email_exists': random.choice(['Y', 'N']),
        'email_creation_days': random.randint(1, 3650),
        
        # Transaction data
        'merchant_ref_number': f"TXN_{random.randint(100000000, 999999999)}",
        'AMOUNT': generate_amount(),
        'Payment_type': random.choice(['CREDIT_CARD', 'DEBIT_CARD', 'PAYPAL', 'BANK_TRANSFER']),
        
        # Analyst and processing data
        'analyst_id': f"ANALYST_{random.randint(100, 999)}",
        'rulecode': f"RULE_{random.randint(1000, 9999)}",
        'datecreated': created_date,
        'ReleaseTime': generate_datetime_string(),
        'rm_order_status': generate_status_code(),
        'action_code': random.randint(100, 999),
        'action_code_text': generate_status_code(),
        'comment': fake.sentence(),
        
        # Geographic and shipping
        'SHIP_TO_COUNTRY': country,
        'bill_country': country,
        'IPAddress': ip_addr,
        
        # Card verification
        'card_type': random.choice(['VISA', 'MASTERCARD', 'AMEX', 'DISCOVER']),
        'avs_match': generate_avs_match(),
        'cvv_match': generate_cvv_match(),
        'bin': generate_bin(),
        
        # Customer names and verification
        'e_name': f"{first_name} {last_name}",
        'first_verification_date': generate_datetime_string(),
        'CUSTOMER_FIRSTNAME': first_name,
        'CUSTOMER_LASTNAME': last_name,
        
        # Community and segment data
        'community_id': f"COMM_{random.randint(1000, 9999)}",
        'segment': random.choice(['PREMIUM', 'STANDARD', 'BASIC', 'VIP']),
        'sub_segment': random.choice(['HIGH_VALUE', 'REGULAR', 'NEW_CUSTOMER', 'RETURNING']),
        'hp_agent_name': fake.name(),
        'affiliate_id': f"AFF_{random.randint(100, 999)}",
        'Score': generate_device_score(),
        
        # Fraud indicators
        'fraud_risk': generate_risk_rating(),
        'fraud_type': random.choice(['IDENTITY_THEFT', 'CARD_FRAUD', 'ACCOUNT_TAKEOVER', 'CLEAN']),
        
        # Billing address
        'BILL_ADDRESS1': fake.street_address(),
        'BILL_ADDRESS2': fake.secondary_address() if random.choice([True, False]) else '',
        'BILL_CITY': city,
        'BILL_STATE': state,
        'BILL_ZIP': fake.zipcode(),
        'BILL_PHONE': generate_phone_number(),
        'BILL_EMAIL': email,
        
        # Name matching and social
        'namematch': random.choice(['EXACT', 'PARTIAL', 'NO_MATCH']),
        'sm_friends': random.randint(0, 1000),
        'source_industry': random.choice(['RETAIL', 'FINANCE', 'TRAVEL', 'GAMING', 'ECOMMERCE']),
        
        # Shipping details
        'SHIPPING_METHOD': random.choice(['STANDARD', 'EXPRESS', 'OVERNIGHT', 'PICKUP']),
        'SHIP_TO_FIRSTNAME': first_name,
        'SHIP_TO_LASTNAME': last_name,
        'SHIP_TO_ADDRESS1': fake.street_address(),
        'SHIP_TO_ADDRESS2': fake.secondary_address() if random.choice([True, False]) else '',
        'SHIP_TO_CITY': city,
        'SHIP_TO_STATE': state,
        'SHIP_TO_ZIP': fake.zipcode(),
        'SHIP_TO_PHONE': generate_phone_number(),
        
        # Email addresses
        'CUSTOMER_EMAIL': email,
        'ship_to_email': email,
        
        # Status and fraud indicators
        'FRAUD_STATUS': generate_status_code(),
        'status': generate_status_code(),
        'Bill2EqualShip2Flag': random.choice(['Y', 'N']),
        
        # Product information
        'product_name': fake.catch_phrase(),
        'merchant_product_sku': f"SKU_{random.randint(100000, 999999)}",
        
        # Hit tracking
        'total_hits': random.randint(1, 100),
        'unique_hits': random.randint(1, 50),
        
        # IP analysis
        'ip_anonymousdetected': random.choice(['Y', 'N']),
        'ip_corporateProxy': random.choice(['Y', 'N']),
        'ip_isp': fake.company(),
        'ip_reputation': generate_risk_rating(),
        'ip_risklevel': generate_domain_risk(),
        'ip_risklevelid': random.randint(1, 4),
        'ip_riskreasonid': random.randint(100, 999),
        'ip_riskscore': generate_device_score(),
        
        # 3D Secure fields
        'cc_3ds_pares_status': random.choice(['Y', 'N', 'U', 'A']),
        'cc_3ds_eci_3ds': random.choice(['01', '02', '05', '06', '07']),
        'cc_3ds_challenge_required': random.choice(['Y', 'N']),
        'cc_3ds_veres_enrolled': random.choice(['Y', 'N', 'U']),
        'cc_3ds_e_commerce_indicator': random.choice(['01', '02', '05', '06', '07'])
    }

def main():
    """Main function to generate the CSV file with fraud prevention dummy data"""
    
    # Define the exact header structure as provided
    headers = [
        'DEVICE_FINGERPRINT', 'DEVICE_FINGERPRINT_SCORE', 'TMX_RISK_RATING',
        'ACCOUNT_EMAIL_SCORE', 'ACCOUNT_TELEPHONE_SCORE', 'SMART_LEARNING_FRAUD_RATING',
        'SMART_LEARNING_RISK_RANK', 'TMX_REASON_CODE', 'ACCOUNT_LOGIN_FIRST_SEEN',
        'ACCOUNT_LOGIN_SCORE', 'ACCOUNT_NAME_SCORE', 'CC_NUMBER_HASH_ASSERT_HISTORY',
        'DEVICE_ASSERT_HISTORY', 'DEVICE_FINGERPRINT_ASSERT_HISTORY', 'FINAL_REVIEW_STATUS',
        'SHIPPING_ADDRESS_ASSERT_HISTORY', 'SHIPPING_ADDRESS_SCORE', 'TMX_POLICY_SCORE',
        'TMX_SUMMARY_REASON_CODE', 'device_id', 'device_first_seen', 'device_score',
        'fuzzy_device_id', 'fuzzy_device_score', 'policy_score', 'reason_code',
        'request_result', 'risk_rating', 'device_id_confidence', 'digital_id_trust_score_rating',
        'true_ip_assert_history', 'true_ip_city', 'ea_advice_id', 'card_type', 'ea_reason',
        'ea_reason_id', 'ea_risk_band_id', 'ea_score', 'ea_status_id', 'domain_exists',
        'domaincorporate', 'domainrelevantinfoID', 'domainrisklevel', 'domainrisklevelID',
        'email', 'email_age', 'email_exists', 'merchant_ref_number', 'analyst_id',
        'rulecode', 'datecreated', 'ReleaseTime', 'rm_order_status', 'action_code',
        'action_code_text', 'comment', 'Payment_type', 'email_creation_days', 'AMOUNT',
        'SHIP_TO_COUNTRY', 'bill_country', 'IPAddress', 'avs_match', 'cvv_match',
        'e_name', 'first_verification_date', 'bin', 'community_id', 'segment',
        'sub_segment', 'hp_agent_name', 'affiliate_id', 'Score', 'CUSTOMER_FIRSTNAME',
        'CUSTOMER_LASTNAME', 'fraud_risk', 'fraud_type', 'BILL_ADDRESS1', 'BILL_ADDRESS2',
        'BILL_CITY', 'BILL_STATE', 'BILL_ZIP', 'BILL_PHONE', 'namematch', 'sm_friends',
        'source_industry', 'SHIPPING_METHOD', 'SHIP_TO_FIRSTNAME', 'SHIP_TO_LASTNAME',
        'SHIP_TO_ADDRESS1', 'SHIP_TO_ADDRESS2', 'SHIP_TO_CITY', 'SHIP_TO_STATE',
        'SHIP_TO_ZIP', 'SHIP_TO_PHONE', 'CUSTOMER_EMAIL', 'BILL_EMAIL', 'FRAUD_STATUS',
        'product_name', 'merchant_product_sku', 'ship_to_email', 'Bill2EqualShip2Flag',
        'status', 'total_hits', 'unique_hits', 'ip_anonymousdetected', 'ip_city',
        'ip_corporateProxy', 'ip_countryCode', 'ip_isp', 'ip_region', 'ip_reputation',
        'ip_risklevel', 'ip_risklevelid', 'ip_riskreasonid', 'ip_riskscore',
        'cc_3ds_pares_status', 'cc_3ds_eci_3ds', 'cc_3ds_challenge_required',
        'cc_3ds_veres_enrolled', 'cc_3ds_e_commerce_indicator'
    ]
    
    print("Generating 1000 rows of fraud prevention dummy data...")
    
    # Generate the CSV file
    filename = 'FQM_Reporting_dummy_data.csv'
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        
        # Write header
        writer.writeheader()
        
        # Generate and write 1000 rows of data
        for i in range(1000):
            row_data = generate_row()
            writer.writerow(row_data)
            
            if (i + 1) % 100 == 0:
                print(f"Generated {i + 1} rows...")
    
    print(f"Successfully generated {filename} with 1000 rows of fraud prevention dummy data!")
    print(f"File saved to: {filename}")

if __name__ == "__main__":
    main()