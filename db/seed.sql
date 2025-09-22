-- =============================
-- Seed data for AI Voice Agent Tool
-- =============================

-- Insert sample agent configurations
INSERT INTO agent_configs (name, description, prompt)
VALUES
(
    'Driver Check-in',
    'Agent calls driver to check load status and ETA',
    '{
        "greeting": "Hi {{driver_name}}, this is Dispatch checking in on load {{load_number}}.",
        "questions": [
            "Can you give me an update on your status?",
            "Where are you currently located?",
            "What is your estimated arrival time?"
        ],
        "logic": {
            "arrival_keywords": ["arrived", "delivered", "drop-off"],
            "delay_keywords": ["stuck", "delayed", "breakdown"]
        }
    }'
),
(
    'Emergency Protocol',
    'Agent detects emergency and escalates to dispatcher',
    '{
        "greeting": "Hi {{driver_name}}, this is Dispatch calling about load {{load_number}}.",
        "emergency_triggers": ["accident", "blowout", "medical", "breakdown"],
        "response": "I understand this is urgent. I will notify a dispatcher immediately to call you back.",
        "escalation": true
    }'
);
