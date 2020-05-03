"""Add name collum on expense table

Revision ID: 5d892343f6a4
Revises: 8e1220123fe0
Create Date: 2020-05-02 17:11:47.480866

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "5d892343f6a4"
down_revision = "8e1220123fe0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("expense", sa.Column("name", sa.String(), nullable=True))
    op.create_index(op.f("ix_expense_name"), "expense", ["name"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_expense_name"), table_name="expense")
    op.drop_column("expense", "name")
    # ### end Alembic commands ###
