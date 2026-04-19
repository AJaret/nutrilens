"""Initial MVP schema.

Revision ID: 20260418_0001
Revises: None
Create Date: 2026-04-18 20:10:00

"""
from __future__ import annotations

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = "20260418_0001"
down_revision = None
branch_labels = None
depends_on = None


sex_enum = postgresql.ENUM("male", "female", name="sex_enum")
activity_level_enum = postgresql.ENUM(
    "sedentary",
    "light",
    "moderate",
    "active",
    "very_active",
    name="activity_level_enum",
)
goal_type_enum = postgresql.ENUM("lose_fat", "maintain", "gain_mass", name="goal_type_enum")
deficit_level_enum = postgresql.ENUM("light", "medium", "aggressive", name="deficit_level_enum")
meal_type_enum = postgresql.ENUM("breakfast", "lunch", "dinner", "snack", name="meal_type_enum")


def upgrade() -> None:
    bind = op.get_bind()
    sex_enum.create(bind, checkfirst=True)
    activity_level_enum.create(bind, checkfirst=True)
    goal_type_enum.create(bind, checkfirst=True)
    deficit_level_enum.create(bind, checkfirst=True)
    meal_type_enum.create(bind, checkfirst=True)

    op.create_table(
        "users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=120), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("password_hash", sa.String(length=255), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table(
        "foods",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("name", sa.String(length=160), nullable=False),
        sa.Column("brand", sa.String(length=160), nullable=True),
        sa.Column("serving_size", sa.Numeric(7, 2), nullable=False),
        sa.Column("serving_unit", sa.String(length=32), nullable=False),
        sa.Column("calories", sa.Numeric(7, 2), nullable=False),
        sa.Column("protein", sa.Numeric(7, 2), nullable=False),
        sa.Column("carbs", sa.Numeric(7, 2), nullable=False),
        sa.Column("fat", sa.Numeric(7, 2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
    )
    op.create_index("ix_foods_name", "foods", ["name"], unique=False)

    op.create_table(
        "user_profiles",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("age", sa.Integer(), nullable=False),
        sa.Column("sex", sex_enum, nullable=False),
        sa.Column("height_cm", sa.Numeric(5, 2), nullable=False),
        sa.Column("weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("activity_level", activity_level_enum, nullable=False),
        sa.Column("goal_type", goal_type_enum, nullable=False),
        sa.Column("deficit_level", deficit_level_enum, nullable=False),
        sa.Column("timezone", sa.String(length=64), nullable=False, server_default="UTC"),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
        sa.UniqueConstraint("user_id", name="uq_user_profiles_user_id"),
    )

    op.create_table(
        "user_goals",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("maintenance_calories", sa.Numeric(7, 2), nullable=False),
        sa.Column("target_calories", sa.Numeric(7, 2), nullable=False),
        sa.Column("target_protein", sa.Numeric(7, 2), nullable=False),
        sa.Column("target_carbs", sa.Numeric(7, 2), nullable=False),
        sa.Column("target_fat", sa.Numeric(7, 2), nullable=False),
        sa.Column("calculated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_user_goals_user_id", "user_goals", ["user_id"], unique=False)

    op.create_table(
        "meals",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("meal_type", meal_type_enum, nullable=False),
        sa.Column("consumed_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("notes", sa.String(length=500), nullable=True),
        sa.Column("total_calories", sa.Numeric(7, 2), nullable=False),
        sa.Column("total_protein", sa.Numeric(7, 2), nullable=False),
        sa.Column("total_carbs", sa.Numeric(7, 2), nullable=False),
        sa.Column("total_fat", sa.Numeric(7, 2), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), server_default=sa.text("now()"), nullable=False),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_meals_user_id", "meals", ["user_id"], unique=False)
    op.create_index("ix_meals_consumed_at", "meals", ["consumed_at"], unique=False)

    op.create_table(
        "meal_items",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("meal_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("food_id", postgresql.UUID(as_uuid=True), nullable=True),
        sa.Column("custom_food_name", sa.String(length=160), nullable=True),
        sa.Column("quantity", sa.Numeric(7, 2), nullable=False),
        sa.Column("unit", sa.String(length=32), nullable=False),
        sa.Column("calories", sa.Numeric(7, 2), nullable=False),
        sa.Column("protein", sa.Numeric(7, 2), nullable=False),
        sa.Column("carbs", sa.Numeric(7, 2), nullable=False),
        sa.Column("fat", sa.Numeric(7, 2), nullable=False),
        sa.ForeignKeyConstraint(["food_id"], ["foods.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["meal_id"], ["meals.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_meal_items_meal_id", "meal_items", ["meal_id"], unique=False)

    op.create_table(
        "weight_logs",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True, nullable=False),
        sa.Column("user_id", postgresql.UUID(as_uuid=True), nullable=False),
        sa.Column("weight_kg", sa.Numeric(5, 2), nullable=False),
        sa.Column("logged_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("note", sa.String(length=255), nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="CASCADE"),
    )
    op.create_index("ix_weight_logs_user_id", "weight_logs", ["user_id"], unique=False)
    op.create_index("ix_weight_logs_logged_at", "weight_logs", ["logged_at"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_weight_logs_logged_at", table_name="weight_logs")
    op.drop_index("ix_weight_logs_user_id", table_name="weight_logs")
    op.drop_table("weight_logs")

    op.drop_index("ix_meal_items_meal_id", table_name="meal_items")
    op.drop_table("meal_items")

    op.drop_index("ix_meals_consumed_at", table_name="meals")
    op.drop_index("ix_meals_user_id", table_name="meals")
    op.drop_table("meals")

    op.drop_index("ix_user_goals_user_id", table_name="user_goals")
    op.drop_table("user_goals")

    op.drop_table("user_profiles")

    op.drop_index("ix_foods_name", table_name="foods")
    op.drop_table("foods")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_table("users")

    bind = op.get_bind()
    meal_type_enum.drop(bind, checkfirst=True)
    deficit_level_enum.drop(bind, checkfirst=True)
    goal_type_enum.drop(bind, checkfirst=True)
    activity_level_enum.drop(bind, checkfirst=True)
    sex_enum.drop(bind, checkfirst=True)
