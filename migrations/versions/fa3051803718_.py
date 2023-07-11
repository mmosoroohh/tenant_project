"""empty message

Revision ID: fa3051803718
Revises: 64604e37c9fb
Create Date: 2023-07-11 18:15:43.872325

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa3051803718'
down_revision = '64604e37c9fb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.alter_column('exclusive',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('tax_amount',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('inclusive',
               existing_type=sa.DOUBLE_PRECISION(precision=53),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transactions', schema=None) as batch_op:
        batch_op.alter_column('inclusive',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('tax_amount',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)
        batch_op.alter_column('exclusive',
               existing_type=sa.String(),
               type_=sa.DOUBLE_PRECISION(precision=53),
               existing_nullable=True)

    # ### end Alembic commands ###
