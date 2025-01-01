CREATE TABLE games (
    gameId VARCHAR(10) PRIMARY KEY NOT NULL,
    season INTEGER,
    week INTEGER,
    gameDate DATE,
    gameTimeEastern TIME,
    homeTeamAbbr VARCHAR(3),
    visitorTeamAbbr VARCHAR(3),
    homeFinalScore INTEGER,
    visitorFinalScore INTEGER
);