#!/usr/bin/python3
DB_ENGINE = "postgresql://postgres:postgres@localhost:5432/ffball"

BASE_URL = "https://www.fantasypros.com"
RANKINGS_URL = BASE_URL + "/nfl/rankings/{}-cheatsheets.php"
STATS_URL = BASE_URL + "/nfl/stats/{}.php"
LOGIN_URL = "https://secure.fantasypros.com/accounts/login/?next=https://www.fantasypros.com/"

FILL_NULL_COLS = ["bye_week", "avg_draft_pick", "fantasy_pts"]
BIO_HEADERS = ["Height", "Weight", "Age", "College"]
RANKINGS_HEADERS = [
    "id",
    "rank",
    "bio_url",
    "name",
    "team",
    "position",
    "position_ranking",
    "bye_week",
    "best_ranking",
    "worst_ranking",
    "avg_ranking",
    "std_dev_ranking",
    "avg_draft_pick",
    "img_url",
    "height",
    "weight",
    "age",
    "college",
]
STATS_HEADERS = {
    "qb": [
        "id",
        "pass_cmp",
        "pass_att",
        "pass_cmp_pct",
        "pass_yds",
        "pass_yds_per_att",
        "pass_td",
        "pass_int",
        "pass_sacks",
        "rush_att",
        "rush_yds",
        "rush_td",
        "fumbles",
        "games",
        "fantasy_pts",
        "fantasy_pts_per_game",
    ],
    "rb": [
        "id",
        "rush_att",
        "rush_yds",
        "rush_yds_per_att",
        "rush_long",
        "rush_20",
        "rush_td",
        "receptions",
        "rec_tgt",
        "rec_yds",
        "rec_yds_per_rec",
        "rec_td",
        "fumbles",
        "games",
        "fantasy_pts",
        "fantasy_pts_per_game",
    ],
    "wr": [
        "id",
        "receptions",
        "rec_tgt",
        "rec_yds",
        "rec_yds_per_rec",
        "rec_long",
        "rec_20",
        "rec_td",
        "rush_att",
        "rush_yds",
        "rush_td",
        "fumbles",
        "games",
        "fantasy_pts",
        "fantasy_pts_per_game",
    ],
    "te": [
        "id",
        "receptions",
        "rec_tgt",
        "rec_yds",
        "rec_yds_per_rec",
        "rec_long",
        "rec_20",
        "rec_td",
        "rush_att",
        "rush_yds",
        "rush_td",
        "fumbles",
        "games",
        "fantasy_pts",
        "fantasy_pts_per_game",
    ],
    "k": [
        "id",
        "field_goals",
        "fg_att",
        "fg_pct",
        "fg_long",
        "fg_1_19",
        "fg_20_29",
        "fg_30_39",
        "fg_40_49",
        "fg_50",
        "extra_points",
        "xp_att",
        "games",
        "fantasy_pts",
        "fantasy_pts_per_game",
    ],
    "dst": [
        "id",
        "sacks",
        "int",
        "fumbles_recovered",
        "fumbles_forced",
        "def_td",
        "safeties",
        "special_teams_td",
        "games",
        "fantasy_pts",
        "fantasy_pts_per_game",
    ],
}
STATS_ALL_HEADERS = [
    "id",
    "pass_cmp",
    "pass_att",
    "pass_cmp_pct",
    "pass_yds",
    "pass_yds_per_att",
    "pass_td",
    "pass_int",
    "pass_sacks",
    "rush_att",
    "rush_yds",
    "rush_yds_per_att",
    "rush_long",
    "rush_20",
    "rush_td",
    "fumbles",
    "receptions",
    "rec_tgt",
    "rec_yds",
    "rec_yds_per_rec",
    "rec_long",
    "rec_20",
    "rec_td",
    "field_goals",
    "fg_att",
    "fg_pct",
    "fg_long",
    "fg_1_19",
    "fg_20_29",
    "fg_30_39",
    "fg_40_49",
    "fg_50",
    "extra_points",
    "xp_att",
    "sacks",
    "int",
    "fumbles_recovered",
    "fumbles_forced",
    "def_td",
    "safeties",
    "special_teams_td",
    "games",
    "fantasy_pts",
    "fantasy_pts_per_game",
]

CREATE_DRAFT_BOARD = """
DROP TABLE IF EXISTS draft_board_{};
CREATE TABLE draft_board_{} (

    id                   INT,
    rank                 INT,
    bio_url              TEXT,
    name                 TEXT,
    team                 TEXT,
    position             TEXT,
    position_ranking     INT,
    bye_week             INT,
    best_ranking         INT,
    worst_ranking        INT,
    avg_ranking          DOUBLE PRECISION,
    std_dev_ranking      DOUBLE PRECISION,
    avg_draft_pick       INT,
    img_url              TEXT,
    height               TEXT,
    weight               TEXT,
    age                  INT,
    college              TEXT,
    pass_cmp             INT,
    pass_att             INT,
    pass_cmp_pct         DOUBLE PRECISION,
    pass_yds             TEXT,
    pass_yds_per_att     DOUBLE PRECISION,
    pass_td              INT,
    pass_int             INT,
    pass_sacks           INT,
    rush_att             INT,
    rush_yds             TEXT,
    rush_yds_per_att     DOUBLE PRECISION,
    rush_long            INT,
    rush_20              INT,
    rush_td              INT,
    fumbles              INT,
    receptions           INT,
    rec_tgt              INT,
    rec_yds              TEXT,
    rec_yds_per_rec      DOUBLE PRECISION,
    rec_long             INT,
    rec_20               INT,
    rec_td               INT,
    field_goals          INT,
    fg_att               INT,
    fg_pct               DOUBLE PRECISION,
    fg_long              INT,
    fg_1_19              INT,
    fg_20_29             INT,
    fg_30_39             INT,
    fg_40_49             INT,
    fg_50                INT,
    extra_points         INT,
    xp_att               INT,
    sacks                INT,
    int                  INT,
    fumbles_recovered    INT,
    fumbles_forced       INT,
    def_td               INT,
    safeties             INT,
    special_teams_td     INT,
    games                INT,
    fantasy_pts          INT,
    fantasy_pts_per_game DOUBLE PRECISION,
    drafted              INT,
    player               TEXT
);
"""
