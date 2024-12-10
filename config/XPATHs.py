login_username_xpath = "//input[@name='username']"
login_password_xpath = "//input[@name='password']"

candidate_details_xpath = "//form/h6[text()='Application Stage']"
candidate_details_fullname_xpath = '//label[text()="Name"]//parent::div/following-sibling::div/p'

save_button_xpath = "//button[text()=' Save ']"
add_button_xpath = "//button[text()=' Add ']"
search_button_xpath = "//button[text()=' Search ']"
submit_button_xpath = "//button[@type='submit']"
edit_button_xpath = '//button/i[@class="oxd-icon bi-pencil-fill"]'


delete_icon_xpath = "//i[@class='oxd-icon bi-trash']"
delete_confirm_button_xpath = "//button[text()=' Yes, Delete ']"


employee_id_xpath = "//label[text()='Employee Id']/parent::div/following::div/input"
employee_details_name_xpath = '//div[@class="orangehrm-edit-employee-imagesection"]//h6[@class="oxd-text oxd-text--h6 --strong"]'
emp_name_xpath = '//div[@class="oxd-grid-4 orangehrm-full-width-grid"]/div[1]//div/input[@placeholder="Type for hints..."]'
emp_edit_info_save_xpath = '//div[@class="orangehrm-horizontal-padding orangehrm-vertical-padding"]//button[text()=" Save "]'


add_candidate_title_xpath = "//h6[@class='oxd-text oxd-text--h6 orangehrm-main-title']"
add_candidate_email_xpath = '//label[text()="Email"]/parent::div/following-sibling::div/input'

search_candidate_xpath = '//label[text()="Candidate Name"]/parent::div/following-sibling::div//input'
search_results_xpath = '//span[@class="oxd-text oxd-text--span"]'

vacancy_name_xpath = '//div/label[text()="Vacancy Name"]/parent::div/following-sibling::div/input'

h5_xpath = "//h5"

job_title_dropdown_xpath = '//i[@class="oxd-icon bi-caret-down-fill oxd-select-text--arrow"]'
job_title_dropdown_options_xpath = '//div[@role="listbox" and @class="oxd-select-dropdown --positon-bottom"]'
hr_manager_dropdown_xpath = '//div[@role="option"]/span[text()="HR Manager"]'

hiring_manager_xpath = '//label[text()="Hiring Manager"]/parent::div/following-sibling::div//input'

buzz_newsfeed_xpath = "//a[text()='Buzz Newsfeed']"
buzz_first_post_date = "//div[@class='oxd-grid-1 orangehrm-buzz-newsfeed-posts']/div[1]//p[@class='oxd-text oxd-text--p orangehrm-buzz-post-time']"
buzz_post_content = "//div[@class='oxd-grid-1 orangehrm-buzz-newsfeed-posts']/div[1]//p[@class='oxd-text oxd-text--p orangehrm-buzz-post-body-text']"
