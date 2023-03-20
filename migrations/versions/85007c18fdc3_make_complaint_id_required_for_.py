"""make complaint id required for transaactions

Revision ID: 85007c18fdc3
Revises: e599051c6dcd
Create Date: 2023-03-20 20:53:27.740427

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '85007c18fdc3'
down_revision = 'e599051c6dcd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.alter_column('complaint_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.alter_column('complaint_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###