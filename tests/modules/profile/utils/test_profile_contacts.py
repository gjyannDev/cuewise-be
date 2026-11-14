"""scrub_contacts: email addresses and phone numbers removed before the résumé text reaches the model (resume-upload
AC6, EC16). The seam is the pure function; the route tests check the model never receives them."""

import pytest

from app.modules.profile.utils.profile_utils import scrub_contacts


def test_a_plain_email_is_removed():
    assert "ana@example.com" not in scrub_contacts("Contact: ana@example.com")


@pytest.mark.parametrize("email", ["ana.maria+jobs@mail.example.co.uk", "A_B-c@sub.domain.io"])
def test_an_email_with_plus_dots_and_subdomains_is_removed(email):
    assert email not in scrub_contacts(f"Email {email} today")


@pytest.mark.parametrize(
    "phone",
    ["+63 917 555 0123", "+1 (415) 555-0134", "(02) 8555-0199", "0917-555-0123", "415.555.0134", "+44 20 7946 0958"],
)
def test_phone_numbers_in_common_formats_are_removed(phone):
    scrubbed = scrub_contacts(f"Phone: {phone} | Remote")

    assert phone not in scrubbed
    assert not any(ch.isdigit() for ch in scrubbed)


def test_several_contacts_in_one_line_are_all_removed():
    scrubbed = scrub_contacts("ana@example.com · +63 917 555 0123 · bo@example.org")

    assert "@" not in scrubbed and "917" not in scrubbed


def test_text_without_contacts_is_unchanged():
    text = "Senior Backend Engineer at Acme (2019-2024)\nBuilt a payments API in Python and Go."

    assert scrub_contacts(text) == text


@pytest.mark.parametrize(
    "text",
    [
        "2019 - 2024",
        "2019-2024",
        "Jan 2020 – Mar 2023",
        "Cut latency by 1200 ms for 10000 users",
        "Python 3.12, Postgres 16",
        "GPA 3.85",
        "Version 1.2.3",
    ],
)
def test_years_ranges_and_plain_numbers_are_not_phone_numbers(text):  # EC16
    assert scrub_contacts(text) == text


def test_two_date_ranges_on_separate_lines_are_not_joined_into_a_phone_number():  # code-derived: the class has no \n
    text = "2019-2024\n2015-2018"

    assert scrub_contacts(text) == text
