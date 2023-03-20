"""#update: All tables with column that has decimal point where set to 2 decimal place

Revision ID: 33658d761777
Revises: 28246604a596
Create Date: 2023-03-04 16:15:59.030891

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '33658d761777'
down_revision = '28246604a596'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('payment_details', 'amount',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('payment_details', 'amount',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###