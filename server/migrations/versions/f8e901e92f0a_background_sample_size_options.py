# pylint: disable=invalid-name
"""Background sample size options

Revision ID: f8e901e92f0a
Revises: df1334fc5fe9
Create Date: 2021-04-06 00:30:45.416380+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f8e901e92f0a"
down_revision = "b91b345bf0a9"
branch_labels = None
depends_on = None


def upgrade():
    op.add_column(
        "election", sa.Column("sample_size_options", sa.JSON(), nullable=True)
    )
    op.add_column(
        "election",
        sa.Column("sample_size_options_task_id", sa.String(length=200), nullable=True),
    )
    op.create_foreign_key(
        op.f("election_sample_size_options_task_id_fkey"),
        "election",
        "background_task",
        ["sample_size_options_task_id"],
        ["id"],
        ondelete="set null",
    )


def downgrade():  # pragma: no cover
    pass
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_constraint(
    #     op.f("election_sample_size_options_task_id_fkey"),
    #     "election",
    #     type_="foreignkey",
    # )
    # op.drop_column("election", "sample_size_options_task_id")
    # op.drop_column("election", "sample_size_options")
    # ### end Alembic commands ###
