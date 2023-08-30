CREATE DATABASE ytbchannels;

CREATE TABLE channels (
    id UUID NOT NULL,
    rank NUMERIC,
    youtuber VARCHAR(150),
    subscribers NUMERIC,
    video_views NUMERIC,
    category VARCHAR(150),
    title VARCHAR(150),
    uploads NUMERIC,
    country VARCHAR(150),
    abbreviation VARCHAR(10),
    channel_type VARCHAR(150),
    video_views_rank NUMERIC,
    country_rank NUMERIC,
    channel_type_rank NUMERIC,
    video_views_for_the_last_month NUMERIC,
    lowest_monthly_earnings NUMERIC,
    highest_monthly_earnings NUMERIC,
    lowest_yearly_earnings NUMERIC,
    highest_yearly_earnings NUMERIC,
    subscribers_for_last_month NUMERIC,
    created_year NUMERIC,
    created_month VARCHAR(10),
    created_date NUMERIC,
    gross_tertiary_education_enrollment_percent DECIMAL,
    population NUMERIC,
    unemployment_rate DECIMAL,
    urban_population NUMERIC,
    latitude DECIMAL,
    longitude DECIMAL,
    PRIMARY KEY (id)
)