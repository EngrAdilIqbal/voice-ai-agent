-- =============================
-- Database schema for AI Voice Agent Tool
-- =============================

-- Table: agent_configs
-- Stores the prompt/logic settings for each agent scenario
CREATE TABLE IF NOT EXISTS agent_configs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL, -- e.g., "Driver Check-in", "Emergency Protocol"
    description TEXT,
    prompt JSONB NOT NULL, -- Stores structured prompts/logic as JSON
    created_at TIMESTAMP DEFAULT NOW()
);

-- Table: call_results
-- Stores the outcome of each test call
CREATE TABLE IF NOT EXISTS call_results (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    call_id TEXT NOT NULL, -- Retell AI call identifier
    agent_config_id UUID REFERENCES agent_configs(id) ON DELETE SET NULL,
    driver_name TEXT,
    driver_phone TEXT,
    load_number TEXT,
    transcript TEXT, -- Full call transcript
    summary JSONB,   -- Structured key-value summary (status, outcome, etc.)
    created_at TIMESTAMP DEFAULT NOW()
);
