import streamlit as st
import pandas as pd
import re

# -------------------------------
# Sample data (your existing data)
# -------------------------------
data = [
    {
        "Profession": "Real Estate Agents", 
        "Pain Points": "Manual effort in creating listings, contracts, and client communication.",
        "Potential Applications": (
            "Automate property listing creation and email follow-ups; "
            "Build tools to manage showings and client preferences; "
            "Generate market trend reports."
        )
    },
    {
        "Profession": "Healthcare Administrators", 
        "Pain Points": "Repetitive administrative tasks like patient scheduling, billing, and compliance reporting.",
        "Potential Applications": (
            "Automate appointment reminders; "
            "Create dashboards for clinic performance; "
            "Simplify compliance reporting."
        )
    },
    {
        "Profession": "Retail Store Managers",
        "Pain Points": "Managing inventory and tracking sales data manually.",
        "Potential Applications": (
            "Automate inventory restocking notifications; "
            "Build tools to analyze sales trends; "
            "Create shift scheduling tools."
        )
    },
    {
        "Profession": "Executive Assistants",
        "Pain Points": "Time-consuming manual scheduling, email organization, and meeting preparation.",
        "Potential Applications": (
            "Automate email filtering and organization; "
            "Build calendar scheduling tools; "
            "Generate meeting preparation documents."
        )
    },
    {
        "Profession": "Office Managers",
        "Pain Points": "Manually tracking office supplies, coordinating staff schedules, and handling reports.",
        "Potential Applications": (
            "Automate supply inventory tracking; "
            "Build tools for staff coordination; "
            "Generate office expense and productivity reports."
        )
    },
    {
        "Profession": "Human Resources Coordinators",
        "Pain Points": "Managing candidate tracking, onboarding processes, and compliance reports manually.",
        "Potential Applications": (
            "Automate candidate tracking systems; "
            "Create onboarding workflows; "
            "Generate compliance and HR analytics reports."
        )
    },
    {
        "Profession": "Data Entry Specialists",
        "Pain Points": "Repetitive manual data entry and database updates.",
        "Potential Applications": (
            "Automate data import workflows; "
            "Build tools for error detection in data entry; "
            "Streamline database updates."
        )
    },
    {
        "Profession": "Receptionists",
        "Pain Points": "Manually managing visitor logs, appointments, and email sorting.",
        "Potential Applications": (
            "Automate visitor log systems; "
            "Create tools for appointment confirmations; "
            "Build email categorization workflows."
        )
    },
    {
        "Profession": "Sales Representatives",
        "Pain Points": "Repetitive CRM updates and follow-up email tasks.",
        "Potential Applications": (
            "Automate CRM updates; "
            "Build tools for personalized email follow-ups; "
            "Generate sales trend reports."
        )
    },
    {
        "Profession": "Real Estate Agents",
        "Pain Points": "Manual effort in creating listings, contracts, and client communication.",
        "Potential Applications": (
            "Automate property listing creation and email follow-ups; "
            "Build tools to manage showings and client preferences; "
            "Generate market trend reports."
        )
    },
    {
        "Profession": "Marketing Specialists",
        "Pain Points": "Time-intensive campaign tracking, analytics, and lead nurturing.",
        "Potential Applications": (
            "Automate campaign performance reports; "
            "Build tools for multi-channel analytics; "
            "Streamline email marketing workflows."
        )
    },
    {
        "Profession": "Social Media Managers",
        "Pain Points": "Managing multi-platform posting schedules and tracking engagement manually.",
        "Potential Applications": (
            "Automate content posting schedules; "
            "Build engagement tracking tools; "
            "Generate multi-platform performance dashboards."
        )
    },
    {
        "Profession": "Advertising Account Executives",
        "Pain Points": "Time-consuming manual campaign performance tracking and client reporting.",
        "Potential Applications": (
            "Automate campaign performance dashboards; "
            "Create tools for personalized client reports; "
            "Streamline proposal generation workflows."
        )
    },
    {
        "Profession": "Healthcare Administrators",
        "Pain Points": "Repetitive administrative tasks like patient scheduling, billing, and compliance reporting.",
        "Potential Applications": (
            "Automate appointment reminders; "
            "Create dashboards for clinic performance; "
            "Simplify compliance reporting."
        )
    },
    {
        "Profession": "Therapists and Counselors",
        "Pain Points": "Manual scheduling, client notes, and billing processes.",
        "Potential Applications": (
            "Automate appointment reminders; "
            "Build tools for client note management; "
            "Streamline billing workflows."
        )
    },
    {
        "Profession": "Medical Office Receptionists",
        "Pain Points": "Managing patient intake forms, insurance verifications, and follow-up reminders manually.",
        "Potential Applications": (
            "Automate patient intake workflows; "
            "Build tools for insurance verification; "
            "Create appointment follow-up systems."
        )
    },
    {
        "Profession": "Fitness Instructors",
        "Pain Points": "Creating personalized workout plans and tracking client progress manually.",
        "Potential Applications": (
            "Automate workout plan generation; "
            "Build tools for client progress tracking; "
            "Schedule session reminders."
        )
    },
    {
        "Profession": "Dietitians and Nutritionists",
        "Pain Points": "Manually creating meal plans and tracking dietary progress for clients.",
        "Potential Applications": (
            "Automate meal plan generation; "
            "Build tools for tracking dietary progress; "
            "Create nutrition education dashboards."
        )
    },
    {
        "Profession": "Retail Store Managers",
        "Pain Points": "Managing inventory and tracking sales data manually.",
        "Potential Applications": (
            "Automate inventory restocking notifications; "
            "Build tools to analyze sales trends; "
            "Create shift scheduling tools."
        )
    },
    {
        "Profession": "Event Planners",
        "Pain Points": "Manual effort in managing RSVPs, budgets, and vendor coordination.",
        "Potential Applications": (
            "Automate RSVP management; "
            "Generate event schedules; "
            "Track deadlines and deliverables."
        )
    },
    {
        "Profession": "Lawyers and Legal Assistants",
        "Pain Points": "Manual document drafting and legal research processes.",
        "Potential Applications": (
            "Automate contract drafting; "
            "Build research tools for legal precedents; "
            "Create billing and deadline tracking systems."
        )
    },
    {
        "Profession": "Nonprofit Administrators",
        "Pain Points": "Manual donor communication and fundraising efforts.",
        "Potential Applications": (
            "Automate donor thank-you emails; "
            "Build volunteer scheduling tools; "
            "Generate impact reports."
        )
    },
    {
        "Profession": "Construction Project Managers",
        "Pain Points": "Manual tracking of project timelines, budgets, and resources.",
        "Potential Applications": (
            "Automate milestone tracking; "
            "Build resource allocation tools; "
            "Create client progress reporting dashboards."
        )
    },
    {
    "Profession": "Accountants and Bookkeepers",
    "Pain Points": "Repetitive data entry and time-consuming report generation.",
    "Potential Applications": (
        "Automate expense categorization; "
        "Create real-time dashboards for financial reporting; "
        "Streamline tax compliance workflows."
    )
    },
    {
        "Profession": "Travel Agents",
        "Pain Points": "Difficulty tracking client preferences and manually building itineraries.",
        "Potential Applications": (
            "Automate itinerary creation; "
            "Build tools to track client preferences; "
            "Generate travel deal recommendations."
        )
    },
    {
        "Profession": "Small Business Owners",
        "Pain Points": "Manual bookkeeping, customer follow-ups, and limited marketing insights.",
        "Potential Applications": (
            "Automate sales and expense tracking; "
            "Build tools for customer loyalty programs; "
            "Generate marketing and sales performance dashboards."
        )
    },
    {
        "Profession": "Restaurant Owners and Managers",
        "Pain Points": "Manually managing reservations, inventory, and staff schedules.",
        "Potential Applications": (
            "Automate reservation systems; "
            "Build tools for inventory tracking; "
            "Create staff scheduling and performance dashboards."
        )
    },
    {
        "Profession": "Beauty Salon Owners and Spa Managers",
        "Pain Points": "Manual appointment booking, inventory of supplies, and staff scheduling.",
        "Potential Applications": (
            "Automate booking and appointment reminders; "
            "Build tools for product and supply tracking; "
            "Create dashboards for revenue and staffing metrics."
        )
    },
    {
        "Profession": "Independent Consultants",
        "Pain Points": "Manual client communication and project tracking.",
        "Potential Applications": (
            "Automate client follow-ups; "
            "Build tools for tracking project progress; "
            "Generate personalized client reports."
        )
    },
    {
        "Profession": "Farmers and Agricultural Managers",
        "Pain Points": "Manually tracking crop data, weather patterns, and resource allocation.",
        "Potential Applications": (
            "Automate crop tracking and yield predictions; "
            "Build tools for resource management; "
            "Create dashboards for weather and market trends."
        )
    },
    {
        "Profession": "Interior Designers",
        "Pain Points": "Difficulty managing client preferences, budgets, and project timelines.",
        "Potential Applications": (
            "Automate budget tracking; "
            "Build tools for managing client design preferences; "
            "Create dashboards for project progress and deadlines."
        )
    },
    {
        "Profession": "Fitness Studio Owners",
        "Pain Points": "Manually managing class schedules and memberships.",
        "Potential Applications": (
            "Automate class booking systems; "
            "Build membership tracking tools; "
            "Create dashboards for revenue and attendance trends."
        )
    },
    {
        "Profession": "E-commerce Entrepreneurs",
        "Pain Points": "Managing product listings, order fulfillment, and customer inquiries across platforms.",
        "Potential Applications": (
            "Automate order status notifications; "
            "Build tools to update inventory across marketplaces; "
            "Create dashboards for sales performance and shipping logistics."
        )
    },
    {
        "Profession": "Educational Administrators",
        "Pain Points": "Manually managing staff schedules, parent communication, and compliance reporting.",
        "Potential Applications": (
            "Automate parent-teacher conference scheduling; "
            "Build dashboards for compliance reports; "
            "Create tools for tracking staff evaluations and student performance."
        )
    },
    {
        "Profession": "Event Venue Managers",
        "Pain Points": "Difficulty managing bookings, staff coordination, and client communications.",
        "Potential Applications": (
            "Automate venue booking systems; "
            "Create tools for staff scheduling; "
            "Build dashboards for revenue tracking and client feedback."
        )
    },
    {
        "Profession": "Retail Buyers",
        "Pain Points": "Manually analyzing sales data and identifying product trends.",
        "Potential Applications": (
            "Automate sales trend analysis; "
            "Build tools for tracking inventory performance; "
            "Generate product restocking recommendations."
        )
    },
    {
        "Profession": "Insurance Agents and Brokers",
        "Pain Points": "Lengthy paperwork, policy comparison, and customer communication.",
        "Potential Applications": (
            "Automate policy quote generation; "
            "Build tools for policy comparison; "
            "Create dashboards for client renewals and communications."
        )
    },
    {
        "Profession": "Property Managers",
        "Pain Points": "Manually tracking maintenance requests, tenant communication, and rent collection.",
        "Potential Applications": (
            "Automate rent collection reminders; "
            "Build tools for tracking maintenance schedules; "
            "Create dashboards for tenant communication and property performance."
        )
    },
    {
        "Profession": "Travel Bloggers",
        "Pain Points": "Manually creating itineraries, tracking expenses, and managing social media content.",
        "Potential Applications": (
            "Automate itinerary and expense tracking; "
            "Build tools for social media content scheduling; "
            "Generate audience engagement analytics."
        )
    },
    {
        "Profession": "Customer Support Managers",
        "Pain Points": "Managing ticket escalations, tracking team performance, and reporting manually.",
        "Potential Applications": (
            "Automate ticket assignment and escalation workflows; "
            "Build tools for team performance tracking; "
            "Create customer satisfaction dashboards."
        )
    },
    {
        "Profession": "Freelance Writers",
        "Pain Points": "Difficulty managing deadlines, client communication, and invoicing.",
        "Potential Applications": (
            "Automate deadline reminders; "
            "Build tools for tracking client communication; "
            "Streamline invoicing workflows."
        )
    },
    {
        "Profession": "Wedding Planners",
        "Pain Points": "Manually coordinating vendor schedules, budgets, and guest lists.",
        "Potential Applications": (
            "Automate vendor scheduling tools; "
            "Build guest list management systems; "
            "Create dashboards for event budgets and timelines."
        )
    },
    {
        "Profession": "Logistics and Supply Chain Coordinators",
        "Pain Points": "Tracking shipments, managing multiple suppliers, and handling inventory data manually.",
        "Potential Applications": (
            "Automate shipment updates; "
            "Build tools for supplier and inventory tracking; "
            "Generate performance and cost-efficiency reports."
        )
    }

]

# Convert initial data to DataFrame
df = pd.DataFrame(data)

# -----------------------------------
# 1. Split potential applications
# -----------------------------------
def split_applications(potential_apps: str):
    """
    Splits the string in 'Potential Applications' into
    separate tasks by semicolons or periods.
    """
    potential_apps = potential_apps.replace('.', ';')
    tasks = [task.strip() for task in potential_apps.split(';') if task.strip()]
    return tasks

# ------------------------------------------------
# 2. Define categories via keyword-based matching
# ------------------------------------------------
categories_dict = [
    # Communication-related tasks
    (r"(reminder|schedule|booking|appointment)",          "reminder notifications"),
    (r"(email|message|communication|follow.?up|campaign)", "customer communication"),  # Renamed from "mass email"
    (r"(crm|client relationship|follow.?up)",             "crm updates"),

    # Reporting and analytics tasks
    (r"(report|analytics|analysis|dashboard|trend)",       "report generator"),
    (r"(performance|evaluation|satisfaction)",            "performance tracking"),

    # Inventory and logistics-related tasks
    (r"(inventory|stock|restock|supply)",                 "inventory management"),
    (r"(shipping|logistics|shipment|fulfillment)",        "shipment tracking"),
    (r"(resource|allocation|budget tracking)",            "resource management"),

    # Compliance and legal tasks
    (r"(compliance|regulation|policy|legal|tax)",         "compliance tasks"),
    
    # Financial tasks
    (r"(billing|invoic|expense|financial|revenue|tax)",   "financial tasks"),

    # Scheduling and coordination
    (r"(calendar|coordination|staff scheduling|shift)",   "calendar and scheduling"),
    (r"(guest list|vendor coordination)",                 "event planning"),

    # Social media and content
    (r"(social media|post|content scheduling|engagement)", "social media management"),

    # Miscellaneous tasks
    (r"(automation|streamline|workflow|tools)",            "workflow automation"),
    # Fallback
    (r".*",                                               "other tasks"),
]


def get_task_category(task_text: str):
    text_lower = task_text.lower()
    for pattern, label in categories_dict:
        if re.search(pattern, text_lower):
            return label
    return "other tasks"

# ------------------------------------------
# 3. Build the expanded DataFrame
# ------------------------------------------
expanded_rows = []
for _, row in df.iterrows():
    profession = row["Profession"]
    pain_points = row["Pain Points"]
    potential_apps = row["Potential Applications"]
    
    tasks = split_applications(potential_apps)
    for task in tasks:
        category = get_task_category(task)
        expanded_rows.append({
            "Profession": profession,
            "Pain Points": pain_points,
            "Automated Task": task,
            "Task Category": category
        })

expanded_df = pd.DataFrame(expanded_rows)

# ------------------------------------------------------
# 4. Streamlit UI
# ------------------------------------------------------
st.title("Automation Opportunities by Profession")

# Sidebar filters
all_categories = sorted(expanded_df["Task Category"].unique())
selected_categories = st.sidebar.multiselect(
    "Filter by Task Category",
    options=all_categories,
    default=all_categories  # By default, show all
)

# Filter the DataFrame based on selection
filtered_df = expanded_df[expanded_df["Task Category"].isin(selected_categories)]

st.markdown("### Filtered Results")
st.dataframe(filtered_df.reset_index(drop=True))

# Show a quick count by category
st.markdown("### Count by Category")
count_by_category = filtered_df["Task Category"].value_counts().reset_index()
count_by_category.columns = ["Task Category", "Count"]
st.dataframe(count_by_category)
